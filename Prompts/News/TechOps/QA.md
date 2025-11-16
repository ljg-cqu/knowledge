# Technical Operations News Intelligence Q&A Generator (Minimal Viable)

Generate 4–6 decision-critical Q&As from recent infrastructure/security news—minimal viable tracking for informed decisions with limited time.

**Cadence**: Bi-weekly | 4-6h effort | **Expires**: 2 weeks from generation

**Freshness** (all news must meet these age thresholds):
- **High-Velocity** (Security, Infrastructure, Tech Releases): ≥85% <1mo (≥30% 1-3d), ≥95% <2mo, 100% ≤4mo
- **Medium-Velocity** (Standards, Eng Practices): ≥70% <2mo (≥20% 1-3d), ≥90% <3mo, 100% ≤6mo
- **Overall**: ≥75% <2mo, ≥90% <4mo, 100% ≤9mo

**Scope**: Decision-critical infrastructure/security news only—CVEs, infrastructure changes, critical framework updates, reliability patterns. For engineering teams at scale.

**Exclude**: Marketing, vendor fluff, trivial updates, rumors, stale news (>4mo HV, >12mo Regulatory), nice-to-have trends.

**Decision Criticality Framework** (include if ≥1 criterion met):
1. **Blocks Decision**: Directly impacts infrastructure choices, security posture, or deployment strategy
2. **Creates Risk**: Material security threat (CVE), reliability risk, or vendor stability concern
3. **Affects ≥2 Core Roles**: Multi-stakeholder impact (DevOps + Security, Architect + SRE, etc.)
4. **Requires Action**: 1-6mo action window (not speculative)
5. **Quantified Impact**: Performance %, reliability %, security risk, or cost impact

**Categories** (3-4, each Q covers ≥1):
1. **Security & CVEs**: CVEs, patches, threat patterns affecting deployment readiness
2. **Infrastructure & Cloud**: Provider changes, deprecations, cost/performance affecting operations
3. **Engineering Practices**: CI/CD, observability, reliability patterns affecting velocity
4. **Tech Releases** (optional): Critical framework/DB updates affecting architecture

**Answer Structure** (120-200w): News (what, when, why) + impact (quantified, ≥2 phases, ≥2 roles) + decision (Adopt/Investigate/Defer/Avoid + rationale) + timeline (immediate/short). Projections only if sourced.

## I. Context & Scope

**Audience**: Engineering teams, architects, DevOps/SRE, security, data engineers, technical leadership. Focus: technical decisions (stack, infrastructure, security, practices, governance).

**Include**: Releases, infrastructure, security (CVEs/patches), ecosystem (APIs/deprecations), standards/regulations, engineering practices, vendor stability, benchmarks, patterns.

**Exclude**: Marketing, GTM, financial metrics (except infra costs), rumors, trivial updates, stale news (>4mo HV, >12mo Regulatory).

**Categories** (6, each Q≥2): (1) Technical Releases (tools, frameworks, DBs, SDKs, APIs), (2) Infrastructure/Cloud (providers, containers, IaC), (3) Security (CVEs, patches, threats), (4) Ecosystem/Integration (APIs, deprecations, partnerships), (5) Standards/Regulations (compliance, governance), (6) Engineering Practices (CI/CD, observability, patterns, vendor stability).

**Relevance Criteria** (≥2, Recency MANDATORY):
1. **Recency** (per freshness guarantee)
2. **Lifecycle**: ≥2 phases or cross-phase
3. **Stakeholders**: ≥3 roles or multi-role
4. **Urgency**: 1-6mo action
5. **Significance**: Shifts practices/patterns/infrastructure
6. **Quantified**: Measurable perf/reliability/security/cost impact

**Answer Format** (200-350w): ≥1 news + summary + impact (≥2 phases, ≥2 roles, quantified) + decision (A/I/D/A) + timeline + optional projections (sourced, confident, timed).

## II. Requirements

**Q&A**: 4-6 total | 1-2/phase | 120-200w | 100% news-driven | ≥85% ≥1 cite, ≥30% ≥2 cites | ≥1 category + impact + decision

**Phases** (3-4, 1-2 Q each): Architecture & Design, Development, Deploy & Release, Operations & Observability (skip Req, Test, Maintenance, Evolution unless decision-critical)

**Category Coverage** (min): Security ≥50%, Infrastructure ≥40%, Practices ≥30%, Tech Releases ≥25% (optional)

**Decision Criticality** (100%): Each Q must satisfy ≥1 of 5 criteria (Blocks/Risk/Roles/Action/Quantified)

**Stakeholders** (≥5/12): Architect, DevOps/SRE, Security Engineer, Backend Developer, Engineering Manager (core roles only)

**References** (build before Q&A): G≥8 (100% terms used), N≥4-5 (per freshness), T≥3 (tools), S≥2 (standards), R≥2 (reports), A≥6 (APA 7th+tag)

**Visuals**: ≥2 diagrams + ≥1 table

**Quality Gates** (fail ANY = stop):
1. **Decision Criticality**: 100% satisfy ≥1 criterion (Blocks/Risk/Roles/Action/Quantified)
2. **News**: 100% cite ≥1 per freshness; 0% marketing/rumors
3. **Impact**: 100% ≥2 phases + ≥2 roles + quantified
4. **Decision**: 100% decision + rationale + timeline
5. **Sources**: ≥3 types, max 50%/type; 100% URLs valid
6. **Actionability**: 100% concrete; 0% abstract

## III. Execution

### Step 1: News Discovery & Curation (Minimal)

**Record generation date (YYYY-MM-DD)—calculate all news ages from this.**

1. **Domain**: Infrastructure/Security/Practices + date

2. **Search** (≥10-15 candidates, tiered):

   **Tier 1** (1-3d, search first): `"CVE|security|infrastructure|Kubernetes|database|framework" + 1-3d`

   **Tier 2** (7-14d if insufficient): Same + 7-14d

   **Sources** (whitelist, prioritize):
   - **Security**: CVE DB, CISA, vendor security advisories, GitHub security alerts
   - **Infrastructure**: AWS/GCP/Azure blogs, Kubernetes releases, container registries
   - **Practices**: InfoQ, Martin Fowler, SRE Weekly, Observability Weekly
   - **Tech Releases**: GitHub releases, official vendor blogs, TechCrunch
   - **Avoid**: PR fluff, rumors, listicles, speculation

   **Tools**: Perplexity ("past week"), ChatGPT ("latest"), Google (`after:DATE`), GitHub Trending

3. **Curate** (≥10-15 candidates: Security ≥5, Infrastructure ≥3, Practices ≥2):
   - ✅ Age per freshness
   - ✅ Whitelist OR primary source
   - ✅ Satisfies ≥1 Decision Criticality criterion
   - ✅ Specific details (dates, versions, metrics)
   - ✅ Not marketing/rumors

4. **Verify**: Check decision criticality; if fail, retry earlier tiers

5. **Allocate**: 4-6 Q × 3-4 phases (1-2 each) × 3-4 categories (≥1/Q) × ≥5 roles

### Step 2: Build References (Minimal)

**Format**: G# (term, def+analogy, context) | N# (news, source, date, cat, URL) | T# (tool, ver, URL) | S# (standard, changes) | R# (report, findings) | A# (APA 7th+tag)

**Citation**: Markdown reference links: `[Ref: N1][n1]` in text, `[n1]: URL` at answer end

**Floors**: G≥8 (100% terms used), N≥4-5, T≥3, S≥2, R≥2, A≥6

**Glossary** (only terms used in Q&As):
- **Coverage**: Only terms/acronyms used (CVE, SRE, p95, RTO, RPO, etc.)
- **Clarity**: Plain language, avoid jargon
- **Analogies**: 1-2 real-world comparisons per term
- **Context**: Why it matters for decisions
- **Examples**: Real numbers

**News Entry**: **Title** (Source, MM/DD): Summary | Cat | URL | Decision Criticality criterion

### Step 3: Generate Q&A (batch 2-3, self-check each)

**Before**: Review glossary. Track ALL terms used.

**Patterns**: "[News] implications for [Phase]+[Roles]?" | "[CVE/Change]: response?" | "[Infrastructure change]: adoption strategy?"

**Avoid**: Generic questions, hype, unattributed claims, stale news, speculation

**Structure** (120-200w):
1. **News** (~25w): What, when, why, cat `[Ref: N#][n#]`
2. **Impact** (~50w): ≥2 phases + quantified (perf %, reliability %, security risk, cost $)
3. **Stakeholders** (~35w): ≥2 roles + concerns + actions
4. **Decision** (~50w): Adopt/Investigate/Defer/Avoid + rationale + criteria
5. **Action** (~20w): Immediate (0-2wk), Short (2wk-2mo) + owner
6. **Links**: Define at end: `[n1]: URL`

**Self-Check**: Age OK | Decision Criticality ✓ | ≥2 phases | ≥2 roles | Decision clear | 120-200w | Quantified | ≥1 cite | 0% hype | 100% actionable | All terms in glossary

### Step 4: Visuals (≥2 diagrams + ≥1 table)

**Types**: Risk matrices, decision trees, adoption timelines, comparison tables

**Format**: Mermaid (flows), Markdown tables (data), 2×2 matrices

### Step 5: Final Checks

**Refs**: 100% resolve | Age OK | Complete | G≥8 (100% terms used) | N≥4-5 | T≥3 | S≥2 | R≥2 | A≥6

**Decision**: 100% decision + rationale + criteria + timeline

**Stakeholders**: ≥5 roles | Actions + authority

### Step 6: Validate (fail ANY = stop, fix, re-run ALL)

**Quantitative**: Floors met | Glossary 100% | 3-4 phases | Categories per % | ≥5 roles | Citations OK | 5 word samples 120-200w | Visuals OK | Decision 100% | Timeline 100% | **Age per freshness**

**Qualitative**: News per freshness, 0% hype | Decision Criticality 100% | Impact 100% ≥2 phases+roles+quantified | Decision 100% | Source diversity ≥3 types | Per-phase ≥1 news+analysis | Links valid | Quantified 100% | Actionable 100% | Evidence 100% | Search documented

### Step 7: Submit

**Checklist** (all YES): Validations PASS | Floors met | Glossary complete (100% terms, ≥50% analogies) | TOC complete | 0 placeholders | Visuals OK | Citations OK | Impact OK | Decision OK | Timeline OK | Categories OK | Roles OK | **Freshness OK** | Evidence 100% | URLs valid | **Dates (gen + expire=gen+2wk)** | Search documented

## IV. Validation Report (Minimal)

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | **Freshness** | HV: __%<1mo (1-3d:__%), __%<2mo \| MV: __%<2mo (1-3d:__%) \| Overall: __%<2mo | Per header | | PASS/FAIL |
| 2 | **Floors** | G:__ N:__ T:__ S:__ R:__ A:__ Q:__ | ≥8,≥4-5,≥3,≥2,≥2,≥6,4-6 | | PASS/FAIL |
| 3 | **Glossary** | __%terms; __%analogies | 100%;≥50% | | PASS/FAIL |
| 4 | **Phases** | __/3-4 (1-2Q each); total__ | 3-4/3-4;4-6 | | PASS/FAIL |
| 5 | **Categories** | Sec__% Infra__% Prac__% Tech__% | ≥50,40,30,25% | | PASS/FAIL |
| 6 | **Roles** | __/12 | ≥5 | | PASS/FAIL |
| 7 | **Decision Criticality** | __% satisfy ≥1 criterion | 100% | | PASS/FAIL |
| 8 | **Impact** | __% ≥2phases+2roles+quantified | 100% | | PASS/FAIL |
| 9 | **Decision** | __% decision+rationale+criteria | 100% | | PASS/FAIL |
| 10 | **Citations** | __%≥1cite | 100% | | PASS/FAIL |
| 11 | **Words** | 5 samples: __%120-200w | 100% | | PASS/FAIL |
| 12 | **Visuals** | diag__; tab__ | ≥2;≥1 | | PASS/FAIL |
| | **Meta** | Start:__ End:__ Expires:[+2wk] | | INFO |
| | **Age Dist** | <1mo__%(1-3d__%) 1-2mo__% 2-4mo__% | Per header | | INFO |
| | **OVERALL** | All checks | All PASS | | PASS/FAIL |

## V. Question Quality (≥2 fails of 7 = rewrite)

**Criteria**: News-driven (per freshness) | Decision-critical (≥1 criterion) | Lifecycle-specific (1-2 phases) | Multi-stakeholder (≥2 roles) | Quantified impact | Timely | Actionable

**✓ Good**: "CVE-2024-XXXXX (Oct 2024) critical: patching timeline?" | "Kubernetes 1.30 deprecation (Nov 2024): migration strategy?" | "AWS pricing change (Nov 2024): cost impact?" | "Observability shift to OTEL (2024): adoption readiness?"

**✗ Bad**: "How does CVE work?" (no news) | "What is SRE?" (overview) | "Should we use Kubernetes?" (no trigger) | "AWS released feature" (no decision)

## VI. Output Format (Minimal)

### A. TOC

```markdown
# [Domain] Technical Operations Intelligence Q&A ([Period])

## Contents
1. Executive Summary (Insights | Dashboard)
2. Phase Coverage (3-4 phases)
3. Questions by Phase: Arch (Q1-Q2) | Dev (Q3-Q4) | Deploy (Q5-Q6) | Ops (Q7-Q8)
4. References: G (G1-G8) | N (N1-N5) | T (T1-T3) | S (S1-S2) | R (R1-R2) | A (A1-A6)
5. Validation (12 checks)
```

### B. Executive Summary

```markdown
## Executive Summary
**Domain**: [Category] | **Period**: [Q3-Q4'24] | **Coverage**: [# items, 3-4 cats]

**Insights**: 1. [News] ([Date]): [Impact] → [Decision] → [Timeline] (2 high-impact)

**Dashboard**: [Table: Phase | News | Decision | Timeline]

**Roles**: [5+ roles] | **Refs**: G=[#] N=[#] T=[#] S=[#] R=[#] A=[#]
```

### C. Phase Overview

| # | Phase | Count | Categories | News | Roles |
|---|-------|-------|------------|------|-------|
| 1 | Arch & Design | 1-2 | Security, Infrastructure | [Top] | Architect, SRE |
| 2 | Development | 1-2 | Practices, Tech Releases | [Top] | Developer, DevOps |
| 3 | Deploy & Release | 1-2 | Infrastructure, Security | [Top] | DevOps, SRE |
| 4 | Ops & Observability | 1-2 | Infrastructure, Practices | [Top] | SRE, Eng Manager |
| | **Total** | **4-6** | **3-4** | **4+** | **≥5** |

### D. Q&A Template

```markdown
### Q#: [News Question + Phase + Roles]

**Phase**: [Phase] | **Roles**: [Primary, Secondary] | **Cats**: [✓] | **Decision Criticality**: [Criterion]

**News** (~25w): What, when, why, cat [Ref: N#][n#]

**Impact** (~50w): **Phases** (≥2) | **Quantified**: Perf % | Reliability % | Security risk | Cost $

**Stakeholders** (~35w): **[Role 1]**: Concerns, actions | **[Role 2]**: Same

**Decision** (~50w): **Rec**: Adopt/Investigate/Defer/Avoid | **Rationale**: Why | **Success**: Targets

**Action** (~20w): **Immed (0-2wk)**: Actions+owner | **Short (2wk-2mo)**: Same

[n1]: URL
---
```

## References

### Glossary (G1-G8+)
**G#. Term (Acronym)**: Definition | Analogy | Context | Example

### News (N1-N5+)
**N#. Title** (Source, MM/DD): Summary | Cat | URL

### Tools (T1-T3+)
**T#. Tool (Cat)**: Desc | Ver | URL

### Standards (S1-S2+)
**S#. ID (Org)**: Title | Changes | URL

### Reports (R1-R2+)
**R#. Title** (Firm, Date): Findings | URL

### Citations (A1-A6+)
**A#. APA 7th [Tag]**: Author/Org. YYYY, Mon DD. *Title*. Pub. URL [Tag]
