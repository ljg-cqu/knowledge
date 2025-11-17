# Technical Operations News Intelligence Q&A Generator

Generate 4-6 decision-critical Q&As from recent infrastructure and security news for engineering teams. Follow this prompt exactly.

**Goal**: Enable informed technical decisions via minimal viable news tracking.

**Cadence**: Bi-weekly | Validity: 2 weeks (re-run after).

**Freshness Thresholds** (all news must meet):
- High-Velocity (Security, Infrastructure, Releases): ≥85% <1mo (≥30% 1-3d), ≥95% <2mo, 100% ≤4mo
- Medium-Velocity (Standards, Practices): ≥70% <2mo (≥20% 1-3d), ≥90% <3mo, 100% ≤6mo
- Overall: ≥75% <2mo, ≥90% <4mo, 100% ≤9mo

**Balance**: Present pros/cons fairly; avoid favoritism; highlight non-fits.

**Decision Criticality Criteria** (≥1 per Q&A):
1. Blocks Decision: Impacts infrastructure/security choices
2. Creates Risk: Material threat/risk/concern
3. Affects ≥2 Roles: Multi-stakeholder impact
4. Requires Action: 1-6mo window
5. Quantified Impact: Measurable perf/reliability/security/cost

## Context & Scope

**Audience**: Architects, DevOps/SRE, Security, Developers, Eng Managers.

**Include**: Releases, infrastructure, security (CVEs), ecosystem, standards, practices, stability, benchmarks.

**Exclude**: Marketing, fluff, trivial, rumors, stale (>4mo HV), non-infra financials.

**Categories** (3-4 per cycle): Technical Releases, Infrastructure/Cloud, Security, Ecosystem/Integration, Standards/Regulations, Engineering Practices.

**Relevance** (≥2 criteria, recency mandatory): Recency, Lifecycle (≥2 phases), Stakeholders (≥3 roles), Urgency (1-6mo), Significance, Quantified.

## Requirements

**Q&A**: 4-6 total | 1-2 per phase | 120-200 words | 100% news-driven | ≥85% ≥1 cite | ≥1 cat + impact + decision

**Phases** (3-4): Architecture & Design, Development, Deploy & Release, Operations & Observability

**Coverage Min**: Security ≥50%, Infrastructure ≥40%, Practices ≥30%, Releases ≥25%

**Criticality**: 100% satisfy ≥1 criterion

**Stakeholders**: 5 core roles, all covered

**References**: G≥8 (all used), N≥4-5 (fresh), T≥3, S≥2, R≥2, A≥6

**Visuals**: ≥2 diagrams + ≥1 table

**Quality Gates** (fail any = stop):
1. Criticality: 100% ≥1 criterion
2. News: 100% cited, fresh; 0% marketing
3. Impact: 100% ≥2 phases + ≥2 roles + quantified
4. Decision: 100% + rationale + timeline
5. Sources: ≥3 types, max 50%/type; URLs valid
6. Actionability: 100% concrete
7. Coverage: MECE decisions, no repeats

## Execution

### 1. News Discovery & Curation

Record generation date (YYYY-MM-DD).

**Search** (≥10-15 candidates, tiered):
- Tier 1 (1-3d): CVE/security/infrastructure/Kubernetes/database/framework + 1-3d
- Tier 2 (7-14d if needed): Same + 7-14d

**Sources** (prioritize whitelist):
- Security: CVE DB, CISA, vendor advisories, GitHub alerts
- Infrastructure: Cloud blogs, Kubernetes, registries
- Practices: InfoQ, Fowler, SRE/Observability Weekly
- Releases: GitHub, vendor blogs, TechCrunch
- Avoid: PR, rumors, speculation

**Tools**: Search engines, GitHub Trending

**Curate** (≥10-15: Security ≥5, Infra ≥3, Practices ≥2):
- Age per freshness
- Whitelist/primary source
- ≥1 criticality criterion
- Specific details
- No marketing/rumors

**Verify**: Criticality; retry if fail

**Allocate**: 4-6 Q&A across 3-4 phases/categories/roles

### 2. Build References

**Format**: G# (term, def+analogy, context) | N# (news, source, date, cat, URL) | T# (tool, ver, URL) | S# (standard, changes) | R# (report, findings) | A# (APA 7th+tag)

**Citation**: [Ref: N#][n#] in text, [n#]: URL at end

**Floors**: G≥8 (all used), N≥4-5, T≥3, S≥2, R≥2, A≥6

**Glossary** (used terms only):
- Plain language, analogies, context, examples

**Evidence**: Prefer primary sources; label uncertainties.

**News Entry**: Title (Source, MM/DD): Summary | Cat | URL | Criticality

### 3. Generate Q&A

**Patterns**: "[News] implications for [Phase]+[Roles]?" | "[CVE/Change]: response?" | "[Change]: adoption strategy?"

**Avoid**: Generic, hype, unattributed, stale, speculation

**Structure** (120-200w):
1. **News** (~25w): What, when, why, cat [Ref: N#][n#]
2. **Impact** (~50w): ≥2 phases + quantified
3. **Stakeholders** (~35w): ≥2 roles + concerns/actions
4. **Decision** (~50w): Rec (Adopt/Investigate/Defer/Avoid) + rationale (trade-offs vs alternatives) + success criteria
5. **Action** (~20w): Immed (0-2wk) + Short (2wk-2mo) + owners
6. Links: [n#]: URL

**Self-Check**: Fresh, criticality, ≥2 phases/roles, word count, quantified, cited, no hype, actionable, terms in glossary, no contradictions, risks flagged, assumptions labeled

### 4. Visuals

≥2 diagrams (Mermaid flows, matrices) + ≥1 table

### 5. Final Checks

Refs: Resolve, fresh, complete, floors met

Decision: 100% + rationale + criteria + timeline

Stakeholders: ≥5 roles + actions

### 6. Validate

**Quantitative**: Floors, glossary 100%, phases/categories/roles, citations, words, visuals, decisions, timelines, freshness

**Qualitative**: Fresh, no hype, criticality 100%, impact 100%, decisions 100%, source diversity, links valid, quantified/actionable/evidence 100%, consistent, risks surfaced

### 7. Submit

**Checklist**: All validations pass, floors met, glossary complete (100% terms, ≥50% analogies), TOC, no placeholders, visuals/citations/impact/decisions/timelines/categories/roles/freshness OK, evidence 100%, URLs valid, dates (gen + expire=gen+2wk), search documented

## Validation Report

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | Freshness | HV: __%<1mo (1-3d:__%), __%<2mo; MV: __%<2mo (1-3d:__%); Overall: __%<2mo | Per thresholds | | PASS/FAIL |
| 2 | Floors | G:__ N:__ T:__ S:__ R:__ A:__ Q:__ | ≥8,≥4-5,≥3,≥2,≥2,≥6,4-6 | | PASS/FAIL |
| 3 | Glossary | __% terms; __% analogies | 100%; ≥50% | | PASS/FAIL |
| 4 | Phases | __/3-4 (1-2Q each); total __ | 3-4/3-4; 4-6 | | PASS/FAIL |
| 5 | Categories | Sec __% Infra __% Prac __% Tech __% | ≥50,40,30,25% | | PASS/FAIL |
| 6 | Roles | __/5 | ≥5 | | PASS/FAIL |
| 7 | Criticality | __% ≥1 criterion | 100% | | PASS/FAIL |
| 8 | Impact | __% ≥2 phases+2 roles+quantified | 100% | | PASS/FAIL |
| 9 | Decision | __% decision+rationale+criteria | 100% | | PASS/FAIL |
| 10 | Citations | __% ≥1 cite | 100% | | PASS/FAIL |
| 11 | Words | 5 samples: __% 120-200w | 100% | | PASS/FAIL |
| 12 | Visuals | diag __; tab __ | ≥2; ≥1 | | PASS/FAIL |
| | Meta | Start: __ End: __ Expires: [+2wk] | | INFO |
| | Age Dist | <1mo __% (1-3d __%) 1-2mo __% 2-4mo __% | Per thresholds | | INFO |
| | OVERALL | All checks | All PASS | | PASS/FAIL |

## Question Quality

**Criteria**: News-driven (fresh), critical (≥1 criterion), phase-specific (1-2), multi-role (≥2), quantified, timely, actionable

**Good**: CVE-XXXX (Oct 2024) critical: patching? | Kubernetes 1.30 deprecation (Nov 2024): migration? | AWS pricing (Nov 2024): cost impact? | OTEL shift (2024): adoption?

**Bad**: How CVE works? (no news) | What is SRE? (overview) | Use Kubernetes? (no trigger) | AWS feature release (no decision)

## Output Format

Produce single Markdown doc: TOC → Executive Summary → Phase Overview → Q&As → References → Validation Report. No planning notes.

### TOC

# [Domain] Technical Operations News Intelligence Q&A ([Period])

## Contents
1. Executive Summary
2. Phase Coverage
3. Questions by Phase (4-6 total)
4. References
5. Validation

### Executive Summary

## Executive Summary
**Domain**: [Category] | **Period**: [Q3-Q4'24] | **Coverage**: [# items, 3-4 cats]

**Insights**: 1. [News] ([Date]): [Impact] → [Decision] → [Timeline] (2 high-impact)

**Dashboard**: [Table: Phase | News | Decision | Timeline]

**Roles**: [5+ roles] | **Refs**: G=[#] N=[#] T=[#] S=[#] R=[#] A=[#]

### Phase Overview

| # | Phase | Count | Categories | News | Roles |
|---|-------|-------|------------|------|-------|
| 1 | Arch & Design | 1-2 | Security, Infrastructure | [Top] | Architect, SRE |
| 2 | Development | 1-2 | Practices, Releases | [Top] | Developer, DevOps |
| 3 | Deploy & Release | 1-2 | Infrastructure, Security | [Top] | DevOps, SRE |
| 4 | Ops & Observability | 1-2 | Infrastructure, Practices | [Top] | SRE, Eng Manager |
| | **Total** | **4-6** | **3-4** | **4+** | **≥5** |

### Q&A Template

### Q#: [News Question + Phase + Roles]

**Phase**: [Phase] | **Roles**: [Primary, Secondary] | **Cats**: [✓] | **Criticality**: [Criterion]

**News**: What, when, why, cat [Ref: N#][n#]

**Impact**: Phases (≥2) | Quantified: Perf % | Reliability % | Security risk | Cost $

**Stakeholders**: **[Role 1]**: Concerns, actions | **[Role 2]**: Same

**Decision**: **Rec**: Adopt/Investigate/Defer/Avoid | **Rationale**: Why (trade-offs vs alternatives) | **Success**: Targets and checks

**Action**: **Immed (0-2wk)**: Actions+owner | **Short (2wk-2mo)**: Same

[n#]: URL
---

## References

### Glossary
**G#. Term**: Definition | Analogy | Context | Example

### News
**N#. Title** (Source, MM/DD): Summary | Cat | URL

### Tools
**T#. Tool**: Desc | Ver | URL

### Standards
**S#. ID**: Title | Changes | URL

### Reports
**R#. Title** (Firm, Date): Findings | URL

### Citations
**A#. APA 7th**: Author/Org. YYYY, Mon DD. *Title*. Pub. URL
