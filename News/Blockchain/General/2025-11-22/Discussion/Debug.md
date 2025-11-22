1. **Q:** Our CFO just said: "Since Bitcoin volatility is macro-driven rather than crypto-structural, we should reduce our liquidity buffer from 18 months to 12 months and invest the savings in growth." What's wrong with that thinking?

   **A:** **Advisor A:** Hold on. That's backwards logic.
   
   **Advisor B:** How so?
   
   **A:** "Macro-driven" doesn't mean lower risk.
   
   **Advisor C:** Right. It actually means crypto is correlated with broader market downturns.
   
   **B:** Mm-hmm. So liquidity needs might actually be higher?
   
   **A:** Exactly. Revenue and external funding will both contract simultaneously during macro stress.
   
   **C:** Let me think through this... A 12-month buffer during a prolonged bear market—let's say 2-3 quarters—
   
   **B:** Leaves only 3-4 months runway at drawdown trough.
   
   **A:** Right. Which forces emergency cost cuts or dilutive financing.
   
   **C:** So the correction: We should maintain or increase the buffer to 18-24 months.
   
   **B:** Precisely. Because macro correlation makes crypto and TradFi funding sources move together.
   
   **A:** Eliminates the diversification benefit.
   
   **C:** Only reduce buffer if revenue diversification away from crypto-correlated sources exceeds 40%.
   
   **B:** Which I doubt we have.
   
   **A:** Agreed.

   **Key Insight:**
   
   | Buffer Strategy | Duration | Bear Market Impact | Remaining Runway | Risk Level |
   |----------------|----------|-------------------|------------------|------------|
   | Proposed (Wrong) | 12 months | 6-9 months | 3-4 months | ⚠️ High |
   | Correct | 18-24 months | 6-9 months | 9-15 months | ✓ Safe |
   
   **Critical Formula:** $\text{Effective Runway} = \text{Buffer} - \text{Bear Market Duration}$
   
   **Reduce buffer only if:** Non-crypto revenue diversification > 40%

2. **Q:** Our engineering lead wants to migrate all smart contracts to Layer-2 within 3 months, testing in production since "Layer-2s are battle-tested." What's the problem?

   **A:** **Security A:** Wait. That's a dangerous conflation.
   
   **Security B:** Exactly. "Battle-tested platforms exist" doesn't mean "our specific contracts are production-ready on Layer-2."
   
   **Engineer C:** What are we missing?
   
   **A:** Smart contract redeployment requires full security audit.
   
   **B:** Plus state migration testing, gradual rollout.
   
   **C:** So rushing to production without audits—
   
   **A:** Exposes users to exploits and state inconsistencies.
   
   **B:** Right. Even minor contract differences between Layer-1 and Layer-2 execution environments can create exploit vectors.
   
   **C:** Good point. What's the historical precedent here?
   
   **A:** Bridge hacks caused over $2 billion in losses in 2024.
   
   **B:** Exactly. Production testing means users lose funds if issues emerge.
   
   **C:** Got it. So what's the proper approach?
   
   **B:** Execute 3-6 month phased migration.
   
   **A:** First, full security audit of Layer-2 deployment. 4-6 weeks.
   
   **C:** Then testnet deployment with simulated volume. 2-3 weeks.
   
   **B:** Mainnet pilot with 10% of volume and rollback capability. 4-6 weeks.
   
   **A:** Then gradual scaling to 100% over 8-12 weeks with continuous monitoring.
   
   **C:** Makes sense. Never test financial infrastructure directly in production.
   
   **B:** Correct.

   **Proper Migration Timeline:**
   
   ```mermaid
   %%{init: {
     "theme": "base",
     "themeVariables": {
       "primaryColor": "#f8f9fa",
       "primaryTextColor": "#1a1a1a",
       "primaryBorderColor": "#7a8591",
       "lineColor": "#8897a8",
       "secondaryColor": "#eff6fb",
       "tertiaryColor": "#f3f5f7"
     }
   }}%%
   gantt
       title Layer-2 Migration Phase Timeline
       dateFormat YYYY-MM-DD
       section Security
       Security Audit           :a1, 2025-01-01, 42d
       section Testing
       Testnet Deployment       :a2, after a1, 17d
       section Rollout
       Mainnet Pilot 10%        :a3, after a2, 35d
       Gradual Scaling to 100%  :a4, after a3, 70d
   ```
   
   | Phase | Duration | Risk | User Exposure |
   |-------|----------|------|---------------|
   | Security Audit | 4-6 weeks | Low | None |
   | Testnet | 2-3 weeks | Low | None |
   | Mainnet Pilot | 4-6 weeks | Medium | 10% volume |
   | Full Rollout | 8-12 weeks | Low | Gradual |
   | **Total** | **3-6 months** | **Managed** | **Protected** |
   
   **Risk Context:** Bridge hacks = $2B+ losses in 2024

3. **Q:** Our PM argues: "Layer-2 takes 3-4 months, cross-chain takes 6-12 months. We need to ship fast, so let's do cross-chain first because it creates a bigger competitive moat." What's wrong?

   **A:** **Product A:** Wait. That inverts prioritization logic.
   
   **Product B:** How so?
   
   **A:** Choosing the longer timeline despite urgency.
   
   **Product C:** Right. And ignoring that Layer-2 is table stakes.
   
   **B:** Mm-hmm. Cross-chain is differentiation, sure.
   
   **A:** But Layer-2 is prerequisite for competitive parity.
   
   **C:** Exactly. Shipping cross-chain without Layer-2 means users still face high fees.
   
   **B:** Which reduces cross-chain feature utility.
   
   **A:** Let me assess the impact... This delays addressing the primary user pain point—high fees—by 6-12 months.
   
   **C:** During which competitors ship Layer-2 and gain users.
   
   **B:** Plus our cross-chain moat is eroded if it's built on slow, expensive Layer-1 foundation.
   
   **A:** True. So here's the correction: Ship Layer-2 first. 3-4 months to achieve cost and speed parity.
   
   **C:** Then layer cross-chain capabilities—additional 6-12 months—on the improved infrastructure.
   
   **B:** What if strategic moat is urgent though?
   
   **A:** Good question. Pursue hybrid.
   
   **C:** Ship Layer-2 for core product while parallel team designs cross-chain.
   
   **B:** Then stagger market launch to avoid user confusion.
   
   **A:** Exactly.

   **Strategy Comparison:**
   
   | Approach | Timeline | User Pain | Competitive Position | Moat Quality |
   |----------|----------|-----------|---------------------|--------------|
   | ❌ Cross-chain first | 6-12 months | High fees persist | Behind on table stakes | Weak (built on slow L1) |
   | ✅ Layer-2 first | 3-4 months → then 6-12 | Resolved quickly | Parity achieved | Strong (built on fast L2) |
   | ✅ Hybrid | Parallel tracks | Resolved in 3-4 months | Best of both | Strongest |
   
   ```mermaid
   %%{init: {
     "theme": "base",
     "themeVariables": {
       "primaryColor": "#f8f9fa",
       "primaryTextColor": "#1a1a1a",
       "primaryBorderColor": "#7a8591",
       "lineColor": "#8897a8",
       "secondaryColor": "#eff6fb",
       "tertiaryColor": "#f3f5f7"
     }
   }}%%
   graph LR
       A[User Needs] --> B[Table Stakes]
       A --> C[Differentiation]
       B --> D[Layer-2 Low Fees]
       C --> E[Cross-Chain]
       D --> F[Competitive Parity]
       E --> G[Competitive Moat]
       F --> G
       
       style B fill:#f1f8f4,stroke:#6b9d7f,stroke-width:2px,color:#1a1a1a
       style D fill:#f1f8f4,stroke:#6b9d7f,stroke-width:2px,color:#1a1a1a
       style F fill:#f1f8f4,stroke:#6b9d7f,stroke-width:2px,color:#1a1a1a
       style E fill:#eff6fb,stroke:#7a9fc5,stroke-width:2px,color:#1a1a1a
   ```

4. **Q:** Our commercial leader says: "TradFi institutions are entering crypto, so we should immediately cut our retail marketing budget by 50% and reallocate entirely to enterprise sales to chase bigger deals." What's the issue?

   **A:** **Strategy A:** That assumes TradFi entry makes retail uncompetitive overnight.
   
   **Strategy B:** But TradFi products will take 12-24 months to scale.
   
   **Strategy C:** Right. And crypto-native features remain differentiated.
   
   **A:** Exactly. DeFi, non-custodial, advanced trading—
   
   **B:** Those stay differentiated for power users.
   
   **C:** Mm-hmm. But abandoning retail eliminates brand awareness and community.
   
   **A:** Which are prerequisites for enterprise trust.
   
   **B:** Let me think through the immediate impact... We lose established retail revenue immediately.
   
   **C:** While enterprise deals have 3-6 month lag before closing.
   
   **A:** Creates a cash flow crisis.
   
   **B:** Plus enterprise buyers evaluate vendors partly on market presence and user base.
   
   **C:** So cutting retail undermines enterprise credibility.
   
   **A:** Exactly. What's the better approach?
   
   **B:** Execute dual strategy with balanced allocation.
   
   **C:** Maintain 70-80% of current retail budget to defend base.
   
   **A:** And add incremental 20-30% for enterprise GTM.
   
   **B:** So increase total commercial budget, don't reallocate.
   
   **C:** Alternative path?
   
   **A:** Segment retail efforts.
   
   **B:** Reduce spend on mass-market acquisition.
   
   **C:** Double down on high-value power-user retention who drive word-of-mouth.
   
   **A:** And enterprise proof points.
   
   **B:** Makes sense.

   **Budget Allocation Strategies:**
   
   | Strategy | Retail % | Enterprise % | Revenue Gap | Enterprise Credibility | Risk |
   |----------|----------|--------------|-------------|----------------------|------|
   | ❌ Proposed | 50% (-50%) | 100% realloc | 3-6 months | Undermined | High |
   | ✅ Dual Strategy | 70-80% | +20-30% new | None | Enhanced | Low |
   | ✅ Segmented | 60-70% focused | +20-30% new | Minimal | Strong | Low |
   
   **Cash Flow Impact:**
   
   ```mermaid
   %%{init: {
     "theme": "base",
     "themeVariables": {
       "primaryColor": "#f8f9fa",
       "primaryTextColor": "#1a1a1a",
       "primaryBorderColor": "#7a8591",
       "lineColor": "#8897a8",
       "secondaryColor": "#eff6fb",
       "tertiaryColor": "#f3f5f7"
     }
   }}%%
   graph TD
       A[Cut Retail 50%] --> B[Immediate Revenue Loss]
       C[Enterprise Sales] --> D[3-6 Month Lag]
       B --> E[Cash Flow Gap]
       D --> E
       E --> F[Crisis]
       
       G[Maintain Retail 70-80%] --> H[Stable Revenue]
       I[Add Enterprise 20-30%] --> J[Gradual Growth]
       H --> K[Healthy Cash Flow]
       J --> K
       
       style B fill:#faf4f4,stroke:#a87a7a,stroke-width:2px,color:#1a1a1a
       style E fill:#faf4f4,stroke:#a87a7a,stroke-width:2px,color:#1a1a1a
       style F fill:#faf4f4,stroke:#a87a7a,stroke-width:2px,color:#1a1a1a
       style H fill:#f1f8f4,stroke:#6b9d7f,stroke-width:2px,color:#1a1a1a
       style K fill:#f1f8f4,stroke:#6b9d7f,stroke-width:2px,color:#1a1a1a
   ```
   
   **Key Insight:** Enterprise buyers evaluate market presence → Retail base = Enterprise credibility

5. **Q:** Our talent leader proposes: "Web3 employment is up 47% and zk engineer demand is up 51%, so we should immediately raise all technical salaries by 50% across the board to stay competitive." What's wrong?

   **A:** **HR A:** Hold on. That confuses demand growth with required salary adjustment.
   
   **HR B:** Exactly. 51% demand increase doesn't translate to 51% salary increase.
   
   **HR C:** What does the actual market data show?
   
   **A:** Market salary data shows 20-30% year-over-year increase for zk engineers.
   
   **B:** Not 50%.
   
   **C:** Right. And across-the-board raises waste budget on roles without supply constraints.
   
   **A:** Like web developers, data analysts.
   
   **B:** Let me calculate the cost impact... Broad 50% raises inflate compensation budget by 40-50%.
   
   **C:** When targeted 20-30% raises for high-demand roles would cost only 8-12% total budget increase.
   
   **A:** Mm-hmm. Overshooting market creates unsustainable cost structure.
   
   **B:** And difficult downward adjustments if market cools.
   
   **C:** So what's the correction?
   
   **A:** Conduct role-specific market analysis.
   
   **B:** Identify high-demand roles—zk, Solidity, Rust.
   
   **C:** Raise those to 75th percentile. Typically 20-30% above current median.
   
   **A:** Leave other roles at market rate. 50th-60th percentile.
   
   **B:** Budget impact: ~10-15% total comp increase versus 50% proposed.
   
   **C:** Same competitive effect for critical roles.
   
   **A:** Exactly.

   **Compensation Strategy Comparison:**
   
   | Approach | Scope | Market Alignment | Budget Impact | Sustainability |
   |----------|-------|------------------|---------------|----------------|
   | ❌ Across-the-board 50% | All roles | Overshoots by 20-30% | +40-50% | Unsustainable |
   | ✅ Targeted 20-30% | High-demand only | 75th percentile | +10-15% | Sustainable |
   
   **Cost Impact Formula:**
   
   $$
   \text{Budget Increase} = \sum_{i=1}^{n} (\text{Role Count}_i \times \text{Salary}_i \times \text{Raise \%}_i)
   $$
   
   **Role-Specific Strategy:**
   
   - **High-demand roles** (zk, Solidity, Rust): 75th percentile = +20-30%
   - **Standard roles** (web dev, analysts): 50th-60th percentile = market rate
   - **Budget impact**: ~10-15% vs. 50% proposed
   
   **Key Misconception:** Demand growth ≠ Salary increase
   
   - 51% demand growth → 20-30% salary increase (not 51%)

6. **Q:** Our strategy officer recommends: "The FSB issued regulatory warnings, so we should immediately relocate the company to El Salvador to avoid compliance costs." What's the flaw?

   **A:** **Compliance A:** Wait. That treats jurisdiction as binary—regulated versus friendly.
   
   **Compliance B:** But FSB warnings signal global regulatory coordination.
   
   **Compliance C:** Right. Relocating to light-touch jurisdictions won't exempt us from regulations where customers reside.
   
   **A:** Exactly. Moving to non-mainstream jurisdictions can trigger loss of banking partners.
   
   **B:** And institutional customers.
   
   **C:** Mm-hmm. Relocating to El Salvador may save initial licensing costs—
   
   **A:** But blocks access to US, EU, Asia institutional customers.
   
   **B:** Who require vendors to be licensed in their jurisdictions.
   
   **C:** Plus loss of USD banking rails is another risk.
   
   **A:** Right. Banks de-risk crypto companies in frontier jurisdictions.
   
   **B:** Could be existential.
   
   **C:** Plus reputational damage from "regulatory arbitrage" perception.
   
   **A:** So what's the better strategy?
   
   **B:** Adopt proactive compliance in major markets.
   
   **C:** EU MiCA, US state-by-state, Singapore, Hong Kong.
   
   **A:** Where customers and revenue are concentrated.
   
   **B:** Use light-touch jurisdictions only for experimental product lines.
   
   **C:** Or as backup entities, not primary operations.
   
   **A:** Exactly. Accept regulatory cost—10-15% opex—as cost of market access.
   
   **B:** Trying to avoid it entirely is false economy.
   
   **C:** Sacrifices 80% of addressable market.
   
   **A:** Agreed.

   **Jurisdiction Strategy Trade-offs:**
   
   | Factor | El Salvador (Light-touch) | Major Markets (Compliant) |
   |--------|---------------------------|---------------------------|
   | **Licensing Costs** | Low | 10-15% opex |
   | **Banking Access** | Limited/None | Full USD rails |
   | **Institutional Customers** | Blocked | Accessible |
   | **Addressable Market** | <20% | 80%+ |
   | **Reputation** | Regulatory arbitrage | Professional |
   | **Sustainability** | High risk | Sustainable |
   
   ```mermaid
   %%{init: {
     "theme": "base",
     "themeVariables": {
       "primaryColor": "#f8f9fa",
       "primaryTextColor": "#1a1a1a",
       "primaryBorderColor": "#7a8591",
       "lineColor": "#8897a8",
       "secondaryColor": "#eff6fb",
       "tertiaryColor": "#f3f5f7"
     }
   }}%%
   graph TD
       A[Relocate to El Salvador] --> B[Save Licensing Costs]
       A --> C[Lose Banking Partners]
       A --> D[Block Institutional Access]
       A --> E[Reputation Damage]
       C --> F[Existential Risk]
       D --> F
       E --> F
       F --> G[80% Market Loss]
       
       H[Comply in Major Markets] --> I[10-15% Opex Cost]
       H --> J[Full Banking Access]
       H --> K[Institutional Trust]
       I --> L[Sustainable Business]
       J --> L
       K --> L
       L --> M[80% Market Access]
       
       style F fill:#faf4f4,stroke:#a87a7a,stroke-width:2px,color:#1a1a1a
       style G fill:#faf4f4,stroke:#a87a7a,stroke-width:2px,color:#1a1a1a
       style L fill:#f1f8f4,stroke:#6b9d7f,stroke-width:2px,color:#1a1a1a
       style M fill:#f1f8f4,stroke:#6b9d7f,stroke-width:2px,color:#1a1a1a
   ```
   
   **Key Insight:** Regulatory cost (10-15% opex) = Cost of market access, not avoidable expense

7. **Q:** Our operations manager says: "The Africa ADAPT initiative is deploying IOTA stablecoins for $70B in trade. We should immediately commit $2M to full integration across all African markets for first-mover advantage." What's wrong?

   **A:** **Strategy A:** Wait. That conflates ADAPT's $70B TAM target with immediate opportunity.
   
   **Strategy B:** And proposes full integration across 54 African countries.
   
   **Strategy C:** When infrastructure maturity varies dramatically by country.
   
   **A:** Right. ADAPT is nascent. Committing $2M before pilot validation is high-risk.
   
   **B:** Spreading $2M across "all African markets"—
   
   **C:** Yields insufficient depth in any single corridor for meaningful volume or learnings.
   
   **A:** Let me do the math... $2M divided by 10 priority corridors equals $200K each.
   
   **B:** But integration costs are estimated at $200K-$500K per corridor.
   
   **C:** For proper implementation—API, compliance, local partnerships, liquidity.
   
   **A:** Mm-hmm. Not continent-wide.
   
   **B:** Plus high risk of total loss if ADAPT regulatory framework stalls.
   
   **C:** Or if IOTA ecosystem remains illiquid.
   
   **A:** What's the better approach?
   
   **B:** Execute focused pilot.
   
   **C:** Select 1-2 high-volume, lower-risk corridors.
   
   **A:** Like Nigeria-Kenya with existing trade volume over $5M monthly.
   
   **B:** Invest $300K-$500K to properly integrate.
   
   **C:** Establish success metrics—cost reduction over 70%, volume over $10M in 6 months.
   
   **A:** Then expand to 2-3 additional corridors only if pilot validates assumptions.
   
   **B:** Exactly. Total risk-adjusted investment: $500K pilot versus $2M blind commitment.
   
   **C:** Makes sense.

   **Investment Strategy Comparison:**
   
   | Approach | Investment | Coverage | Per-Corridor Depth | Risk | Learning Potential |
   |----------|------------|----------|-------------------|------|-------------------|
   | ❌ Full Integration | $2M | 10+ corridors | $200K (insufficient) | Total loss risk | Diluted |
   | ✅ Focused Pilot | $300K-$500K | 1-2 corridors | $300K-$500K (proper) | Limited downside | High-quality |
   
   **Integration Cost Breakdown:**
   
   $$
   \text{Cost per Corridor} = \text{API} + \text{Compliance} + \text{Partnerships} + \text{Liquidity} = \$200\text{K}-\$500\text{K}
   $$
   
   **Pilot Success Metrics:**
   
   - **Cost reduction**: >70%
   - **Volume target**: >$10M in 6 months
   - **Corridor example**: Nigeria-Kenya ($5M+ monthly existing trade)
   
   ```mermaid
   %%{init: {
     "theme": "base",
     "themeVariables": {
       "primaryColor": "#f8f9fa",
       "primaryTextColor": "#1a1a1a",
       "primaryBorderColor": "#7a8591",
       "lineColor": "#8897a8",
       "secondaryColor": "#eff6fb",
       "tertiaryColor": "#f3f5f7"
     }
   }}%%
   graph TD
       A[$2M Full Integration] --> B[Spread Across 10+ Corridors]
       B --> C[$200K Each]
       C --> D[Insufficient Depth]
       D --> E[No Meaningful Results]
       E --> F[Total Loss Risk]
       
       G[$500K Focused Pilot] --> H[1-2 High-Volume Corridors]
       H --> I[$300K-$500K Each]
       I --> J[Proper Integration]
       J --> K{Validate?}
       K -->|Yes| L[Expand 2-3 More]
       K -->|No| M[Limited Loss]
       
       style D fill:#faf6f0,stroke:#a89670,stroke-width:2px,color:#1a1a1a
       style F fill:#faf4f4,stroke:#a87a7a,stroke-width:2px,color:#1a1a1a
       style J fill:#f1f8f4,stroke:#6b9d7f,stroke-width:2px,color:#1a1a1a
       style L fill:#f1f8f4,stroke:#6b9d7f,stroke-width:2px,color:#1a1a1a
   ```
   
   **Key Misconception:** $70B TAM ≠ Immediate opportunity (nascent initiative)

8. **Q:** Our CEO announces: "Bitcoin reached $126K and market cap exceeded $4T, proving crypto has achieved mainstream stability. We should leverage our balance sheet and borrow to buy $50M in Bitcoin as a treasury reserve asset." What's the problem?

   **A:** **CFO A:** Hold on. That interprets a price peak as "stability."
   
   **CFO B:** But the document describes a 30% drawdown.
   
   **CFO C:** Right. $126K down to under $86K within the same reporting period.
   
   **A:** This is evidence of extreme volatility, not stability.
   
   **B:** Mm-hmm. Using leverage amplifies downside.
   
   **C:** If BTC drops another 30%—
   
   **A:** We face margin calls or $15M-plus loss.
   
   **B:** Let me calculate the impact... A leveraged $50M BTC position with 30% drawdown creates $15M unrealized loss.
   
   **C:** Potential margin call requiring $5M-$10M additional collateral.
   
   **A:** For most companies, that magnitude of non-operational loss threatens liquidity.
   
   **B:** Plus employee confidence, stakeholder trust.
   
   **C:** If using 2:1 leverage, a 50% BTC decline wipes out the entire position.
   
   **A:** So what's the correction?
   
   **B:** Treat 30%-plus monthly volatility as disqualifying for leveraged treasury allocation.
   
   **C:** If strategic BTC exposure is desired, limit to 5-10% of liquid reserves.
   
   **A:** Not 50%-plus.
   
   **B:** Use zero leverage—cash purchase only.
   
   **C:** And only deploy capital that can sustain 50-70% drawdown without operational impact.
   
   **A:** For most firms, BTC treasury allocation should be 0%.
   
   **B:** Until revenue stability and multi-year profitability are established.
   
   **C:** Agreed.

   **Volatility Reality Check:**
   
   | Metric | Value | Interpretation |
   |--------|-------|----------------|
   | Peak price | $126K | Not "stability" |
   | Drawdown | 30% ($126K → $86K) | Extreme volatility |
   | Same period | Yes | Evidence against stability |
   
   **Leverage Risk Analysis:**
   
   | Scenario | Position Size | Leverage | BTC Drop | Loss | Additional Risk |
   |----------|--------------|----------|----------|------|-----------------|
   | ❌ Proposed | $50M | 2:1 | 30% | $15M | Margin call: $5M-$10M |
   | ❌ Worst Case | $50M | 2:1 | 50% | $25M | Position wiped out |
   | ✅ Conservative | 5-10% reserves | None | 50-70% | Sustainable | No operational impact |
   
   **Loss Calculation:**
   
   $$
   \text{Leveraged Loss} = \text{Position Size} \times \text{Drawdown \%} \times \text{Leverage Factor}
   $$
   
   **Example:** $50M × 30\% × 2 = $30M exposure → $15M loss
   
   ```mermaid
   %%{init: {
     "theme": "base",
     "themeVariables": {
       "primaryColor": "#f8f9fa",
       "primaryTextColor": "#1a1a1a",
       "primaryBorderColor": "#7a8591",
       "lineColor": "#8897a8",
       "secondaryColor": "#eff6fb",
       "tertiaryColor": "#f3f5f7"
     }
   }}%%
   graph TD
       A[$50M Leveraged BTC] --> B[30% Drawdown]
       B --> C[$15M Unrealized Loss]
       C --> D[Margin Call]
       D --> E[$5M-$10M Collateral Needed]
       E --> F[Liquidity Threat]
       F --> G[Employee & Stakeholder Crisis]
       
       H[Conservative: 5-10% Reserves] --> I[Zero Leverage]
       I --> J[Cash Purchase Only]
       J --> K[50-70% Drawdown Sustainable]
       K --> L[No Operational Impact]
       
       style C fill:#faf6f0,stroke:#a89670,stroke-width:2px,color:#1a1a1a
       style D fill:#faf4f4,stroke:#a87a7a,stroke-width:2px,color:#1a1a1a
       style F fill:#faf4f4,stroke:#a87a7a,stroke-width:2px,color:#1a1a1a
       style G fill:#faf4f4,stroke:#a87a7a,stroke-width:2px,color:#1a1a1a
       style K fill:#f1f8f4,stroke:#6b9d7f,stroke-width:2px,color:#1a1a1a
       style L fill:#f1f8f4,stroke:#6b9d7f,stroke-width:2px,color:#1a1a1a
   ```
   
   **Critical Rules:**
   
   - **Treasury allocation**: 0% for most firms (until multi-year profitability)
   - **If exposure desired**: Max 5-10% of liquid reserves
   - **Leverage**: Zero (cash only)
   - **Volatility threshold**: >30% monthly = disqualifying
   
   **Key Misconception:** Price peak ≠ Stability (30% drawdown = extreme volatility)
