# Technical Operations News Intelligence Q&A Generator

Generate 4-6 decision-critical Q&As from recent infrastructure and security news for engineering teams.

**Goal**: Enable informed technical decisions via minimal viable news tracking.

**Cadence**: Bi-weekly | Validity: 2 weeks

**Freshness**:
- Security/Infrastructure/Releases: ≥80% <1mo, 100% <4mo
- Standards/Practices: ≥70% <2mo, 100% <6mo

**Balance**: Present pros/cons fairly; avoid favoritism; highlight non-fits.

**Decision Criticality** (≥1 per Q&A):
1. Blocks Decision: Impacts infrastructure/security choices
2. Creates Risk: Material threat/concern
3. Affects ≥2 Roles: Multi-stakeholder impact
4. Requires Action: 1-6mo window
5. Quantified Impact: Measurable metrics

## Context & Scope

**Audience**: Architects, DevOps/SRE, Security, Developers, Eng Managers.

**Include**: Releases, infrastructure, security (CVEs), ecosystem, standards, practices, benchmarks.

**Exclude**: Marketing, trivial, rumors, stale (>4mo security), non-infra topics.

**Categories**: Technical Releases, Infrastructure/Cloud, Security, Ecosystem/Integration, Standards/Regulations, Engineering Practices.

**Relevance** (≥2 criteria): Recency, Lifecycle (≥2 phases), Stakeholders (≥2 roles), Urgency (1-6mo), Quantified impact.

## Requirements

**Q&A**: 4-6 total | 120-200 words | 100% news-driven + cited | category + impact + decision

**Phases**: Architecture & Design, Development, Deploy & Release, Operations & Observability

**Coverage**: Security ≥50%, Infrastructure ≥40%, Practices ≥30%, Releases ≥25%

**Stakeholders**: ≥5 core roles covered

**References**: Glossary ≥8, News ≥4, Tools ≥3, Standards ≥2, Reports ≥2, Citations ≥6

**Visuals**: ≥2 diagrams + ≥1 table

**Quality Gates**:
1. Criticality: 100% meet ≥1 criterion
2. News: Fresh, cited, no marketing
3. Impact: ≥2 phases + ≥2 roles + quantified
4. Decision: Recommendation + rationale + timeline
5. Sources: ≥3 types, diverse; URLs valid
6. Actionability: Concrete actions with owners

## Execution

### 1. News Discovery & Curation

Record generation date (YYYY-MM-DD).

**Search** (≥10 candidates):
- Priority: 1-7d for security/infrastructure
- Fallback: 7-30d as needed

**Sources**:
- Security: CVE DB, CISA, vendor advisories, GitHub
- Infrastructure: Cloud blogs, Kubernetes, registries
- Practices: InfoQ, Fowler, SRE Weekly
- Releases: GitHub, vendor blogs
- Avoid: PR, rumors, speculation

**Curate** (Security ≥5, Infrastructure ≥3, Practices ≥2):
- Fresh per thresholds
- Primary sources preferred
- Meets ≥1 criticality criterion
- Specific, quantified details

**Allocate**: 4-6 Q&As across phases/categories/roles

### 2. Build References

**Format**: 
- G# (term, def+analogy, context)
- N# (news, source, date, cat, URL)
- T# (tool, ver, URL)
- S# (standard, changes)
- R# (report, findings)
- A# (APA 7th)

**Citation**: [Ref: N#][n#] in text, [n#]: URL at end

**Glossary**: Plain language + analogies + context; used terms only

**Evidence**: Prefer primary sources; label uncertainties

### 3. Generate Q&A

**Patterns**: "[News] implications for [Phase]+[Roles]?" | "[CVE/Change]: response?" | "[Change]: adoption strategy?"

**Avoid**: Generic, hype, unattributed, stale, speculation

**Structure** (120-200w total):
1. **News**: What, when, why, category [Ref: N#][n#]
2. **Impact**: ≥2 phases + quantified metrics
3. **Stakeholders**: ≥2 roles + concerns/actions
4. **Decision**: Recommendation (Adopt/Investigate/Defer/Avoid) + rationale + success criteria
5. **Action**: Immediate (0-2wk) + Short-term (2wk-2mo) + owners
6. **Links**: [n#]: URL

**Self-Check**: Fresh, meets criticality, ≥2 phases/roles, quantified, cited, actionable, terms in glossary, risks flagged

### 4. Visuals

≥2 diagrams (Mermaid flows, matrices) + ≥1 table

### 5. Validate & Submit

**Quantitative**: Reference floors met, phases/categories/roles covered, citations present, word count, visuals included, freshness thresholds

**Qualitative**: Fresh news, no hype, criticality met, impact quantified, decisions with rationale, source diversity, URLs valid, risks surfaced

**Submit**: All validations pass, glossary complete, TOC included, dates (generation + expiry=gen+2wk)

## Validation Report

| # | Check | Criteria | Result | Status |
|---|-------|----------|--------|--------|
| 1 | Freshness | Sec/Infra ≥80% <1mo; Stds/Prac ≥70% <2mo | | PASS/FAIL |
| 2 | References | G≥8, N≥4, T≥3, S≥2, R≥2, A≥6 | | PASS/FAIL |
| 3 | Q&As | 4-6 total, 120-200w each | | PASS/FAIL |
| 4 | Coverage | Sec≥50%, Infra≥40%, Prac≥30%, Rel≥25% | | PASS/FAIL |
| 5 | Roles | ≥5 roles covered | | PASS/FAIL |
| 6 | Criticality | 100% meet ≥1 criterion | | PASS/FAIL |
| 7 | Impact | 100% with ≥2 phases+roles, quantified | | PASS/FAIL |
| 8 | Decision | 100% with recommendation+rationale | | PASS/FAIL |
| 9 | Citations | All Q&As cited with URLs | | PASS/FAIL |
| 10 | Visuals | ≥2 diagrams, ≥1 table | | PASS/FAIL |
| | Dates | Gen: __ | Expires: [+2wk] | INFO |
| | OVERALL | All checks PASS | | PASS/FAIL |

## Question Quality

**Criteria**: Fresh news, critical, multi-role (≥2), quantified, actionable

**Good**: CVE-XXXX critical: patching strategy? | K8s 1.30 deprecation: migration? | AWS pricing change: cost impact?

**Bad**: How CVE works? | What is SRE? | Use Kubernetes? | Feature without decision impact

## Output Format

Single Markdown doc: TOC → Executive Summary → Phase Overview → Q&As → References → Validation

### TOC Structure

```
# [Domain] Technical Operations News Intelligence Q&A ([Period])

## Contents
1. Executive Summary
2. Phase Coverage
3. Questions by Phase (4-6)
4. References
5. Validation
```

### Executive Summary

**Domain**: [Category] | **Period**: [Dates] | **Coverage**: [# items, categories]

**Key Insights**: 1-2 high-impact decisions with news, impact, recommendation, timeline

**Dashboard**: Table with Phase | News | Decision | Timeline

**Roles**: 5+ roles | **References**: G/N/T/S/R/A counts

### Phase Overview Table

| Phase | Categories | Top News | Roles |
|-------|------------|----------|-------|
| Arch & Design | Security, Infrastructure | [Item] | Architect, SRE |
| Development | Practices, Releases | [Item] | Developer, DevOps |
| Deploy & Release | Infrastructure, Security | [Item] | DevOps, SRE |
| Ops & Observability | Infrastructure, Practices | [Item] | SRE, Manager |

### Q&A Template

```
### Q#: [News Question + Phase + Roles]

**Phase**: [Phase] | **Roles**: [Primary, Secondary] | **Category**: [Type] | **Criticality**: [Criterion]

**News**: What, when, why [Ref: N#][n#]

**Impact**: Phases (≥2), quantified metrics (perf/reliability/security/cost)

**Stakeholders**: 
- **[Role 1]**: Concerns, actions
- **[Role 2]**: Concerns, actions

**Decision**: 
- **Recommendation**: Adopt/Investigate/Defer/Avoid
- **Rationale**: Trade-offs vs alternatives
- **Success Criteria**: Targets

**Action**: 
- **Immediate (0-2wk)**: Actions + owner
- **Short-term (2wk-2mo)**: Actions + owner

[n#]: URL
```

## References Format

**Glossary (G#)**: Term | Definition + Analogy | Context

**News (N#)**: Title (Source, MM/DD) | Summary | Category | URL

**Tools (T#)**: Name | Description | Version | URL

**Standards (S#)**: ID | Title | Key Changes | URL

**Reports (R#)**: Title (Firm, Date) | Key Findings | URL

**Citations (A#)**: APA 7th format with URL
