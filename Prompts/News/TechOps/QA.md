# Technical Operations News Intelligence Q&A Generator

## Table of Contents
- [Overview](#overview)
- [Scope](#scope)
- [Requirements](#requirements)
- [Execution](#execution)
- [Validation Checklist](#validation-checklist)
- [Question Quality](#question-quality)
- [Output Format](#output-format)
- [Glossary](#glossary)

## Overview

**Problem**: Engineering teams lack time-efficient, decision-focused technical news filtering, leading to missed critical security/infrastructure updates or information overload.

**Task**: Generate 4-6 decision-critical Q&As from infrastructure and security news for engineering teams.

**Goal**: Enable informed technical decisions via minimal viable news tracking.

**Constraints**: Bi-weekly cadence, 2-week validity, primary sources only

**Freshness Thresholds**:
- Security/Infrastructure/Releases: ≥80% <1mo, 100% <4mo
- Standards/Practices: ≥70% <2mo, 100% <6mo

**Decision Criticality** (≥1 required per Q&A):
1. Blocks infrastructure/security decisions (vendor choice, architecture)
2. Creates material risk (security breach, outage, compliance violation)
3. Impacts ≥2 roles (cross-team coordination required)
4. Time-sensitive (action window 1-6mo)
5. Quantified impact (measurable performance/cost/security metrics)

## Scope

**Audience**: Architects, DevOps/SRE, Security Engineers, Developers, Engineering Managers

**Categories** (include): Security (CVEs), Infrastructure/Cloud, Technical Releases, Standards/Regulations, Engineering Practices, Ecosystem/Integration

**Exclude**: Marketing, rumors, speculation, stale news (>4mo security, >6mo practices)

**Relevance Criteria** (≥2 required per Q&A): 
- Recency: <1mo (security), <2mo (practices)
- Multi-phase: ≥2 lifecycle phases impacted
- Multi-role: ≥2 distinct roles impacted
- Time-sensitive: action window 1-6mo
- Quantified: specific metrics with units

## Requirements

**Q&A Structure**: 4-6 total, 120-200 words each, cited sources with URLs

**Lifecycle Phases**: Architecture & Design, Development, Deploy & Release, Operations & Observability

**Topic Priority** (coverage order):
1. **Critical**: Security (CVEs, vulnerabilities), Infrastructure (cloud, networking)
2. **Important**: Practices (DevOps, SRE), Major releases (breaking changes)
3. **Optional**: Ecosystem updates (adoption <5%)

**Coverage**:
- **Roles**: ≥5 distinct roles across all Q&As
- **News Sources**: ≥4 primary sources (N#)
- **Visuals**: ≥2 diagrams, ≥1 table

**References Types**: G# (Glossary), N# (News), T# (Tools), S# (Standards), R# (Reports), A# (Citations)

## Execution

### 1. News Discovery & Curation

**Search** (≥10 candidates; prioritize 1-7d for security/infrastructure):
- **Security**: CVE DB, CISA KEV, vendor advisories, GitHub Security Advisories
- **Infrastructure**: AWS/GCP/Azure blogs, Kubernetes blog, CNCF
- **Practices**: InfoQ, Martin Fowler blog, SRE Weekly
- **Releases**: GitHub releases, vendor blogs, package registries

**Filter**:
- Primary sources only (vendor announcements, CVE DB, official docs)
- Meet freshness thresholds + ≥1 criticality criterion
- Quantified details present
- Balanced across categories

**Allocate**: Distribute 4-6 Q&As across phases, categories, roles. Record date (YYYY-MM-DD).

### 2. Build References

**Reference Format**:
- **G#**: term, definition with analogy (only used terms)
- **N#**: title, source, YYYY-MM-DD, category, URL
- **T#**: name, description, version, URL
- **S#**: ID, title, key changes, URL
- **R#**: title, firm, date, key findings, URL
- **A#**: APA 7th with URL

**Citation**: [Ref: N#][n#] inline → [n#]: URL at end

**Evidence**: Primary sources only; flag uncertainties ("estimated", "unconfirmed")

### 3. Generate Q&A

**Question Format**: "[News] implications for [Phase]+[Roles]?" or "[CVE/Change]: response strategy?"

**Avoid**: Generic questions, hype, unattributed claims, speculation

**Structure** (120-200 words):
1. **News**: What, when, why, category [Ref: N#][n#]
2. **Impact**: ≥2 phases, quantified metrics (latency/cost/severity)
3. **Stakeholders**: ≥2 roles, concerns, actions
4. **Decision**: 
   - **Alternatives**: ≥2 options (cost $, benefit with metric, risk probability/impact)
   - **Recommendation**: Adopt/Investigate/Defer/Avoid + rationale
   - **Success Criteria**: baseline → target, measurement method
   - **Limitations**: When NOT to use, counterarguments
5. **Action**: Immediate (0-2wk), short-term (2wk-2mo), owners
6. **Links**: [n#]: URL

### 4. Add Visuals

Include ≥2 diagrams (Mermaid) + ≥1 table

### 5. Validate & Submit

**Check**:
- **Completeness**: N≥4, 5+ roles, 4-6 Q&As, 120-200w/Q&A, URLs valid, ≥2 diagrams, ≥1 table
- **Quality**: Freshness met, ≥1 criticality/Q&A, quantified metrics, no hype/speculation
- **Decisions**: ≥2 alternatives (cost/benefit/risk), recommendation+rationale, success criteria (baseline→target), limitations
- **Accuracy**: Facts verified (primary sources), contradictions checked, uncertainties flagged

**Submit**: Glossary (used terms only), TOC, generation date, expiry (date+2wk)

## Validation Checklist

| Check | Criteria | Status |
|-------|----------|--------|
| Freshness | Sec/Infra ≥80% <1mo; Stds/Prac ≥70% <2mo | ☐ |
| References | N≥4 primary sources | ☐ |
| Q&As | 4-6 total, 120-200w each | ☐ |
| Priority | Security/Infrastructure emphasized | ☐ |
| Roles | ≥5 distinct roles | ☐ |
| Criticality | Each Q&A: ≥1 criterion | ☐ |
| Impact | Each Q&A: ≥2 phases+roles, quantified | ☐ |
| Decision | Each Q&A: ≥2 alternatives, recommendation, criteria, limitations | ☐ |
| Citations | All URLs valid | ☐ |
| Accuracy | Facts verified, contradictions checked, uncertainties flagged | ☐ |
| Visuals | ≥2 diagrams, ≥1 table | ☐ |
| Dates | Generation: ___ \| Expiry: ___ (+2wk) | ☐ |

## Question Quality

**Good**: News-driven, decision-focused, quantified
- "CVE-2024-XXXX (CVSS 9.8): patching strategy?"
- "K8s 1.30 deprecations: migration approach?"
- "AWS pricing +20%: cost impact?"

**Bad**: Generic, educational, no trigger
- "How do CVEs work?"
- "What is SRE?"
- "Should we use Kubernetes?"

## Output Format

Single Markdown document with sections: **TOC** → **Executive Summary** → **Phase Overview** → **Q&As** → **References** → **Validation**

### Executive Summary

**Domain**: TechOps | **Period**: YYYY-MM-DD to YYYY-MM-DD | **Coverage**: X Q&As, Y phases

**Key Insights** (top 1-2 by impact):
- News + quantified impact + recommendation + timeline

**Dashboard**:

| Phase | News | Decision | Timeline |
|-------|------|----------|----------|
| [Phase] | [Item] | [Adopt/Defer/etc] | [Xmo] |

**Stats**: X roles, N# news, T# tools, S# standards

### Phase Overview

| Phase | Categories | Top News | Roles |
|-------|------------|----------|-------|
| Architecture & Design | Security, Infrastructure | [Item] | Architect, SRE |
| Development | Practices, Releases | [Item] | Developer, DevOps |
| Deploy & Release | Infrastructure, Security | [Item] | DevOps, SRE |
| Operations & Observability | Infrastructure, Practices | [Item] | SRE, Manager |

### Q&A Template

```markdown
### Q#: [News Question + Phase + Roles]

**Phase**: [Phase] | **Roles**: [Role1, Role2] | **Category**: [Category] | **Criticality**: [#]

**News**: [What] on YYYY-MM-DD: [why] [Ref: N#][n#]

**Impact**: 
- **[Phase 1]**: [metric with unit] (latency +50ms, cost +$2K/mo, CVSS 9.8)
- **[Phase 2]**: [metric with unit]

**Stakeholders**: 
- **[Role 1]**: [concern] → [action]
- **[Role 2]**: [concern] → [action]

**Decision**: 
- **Alternatives**: 
  - A: [description] | Cost: $ | Benefit: [metric] | Risk: [probability/impact]
  - B: [description] | Cost: $ | Benefit: [metric] | Risk: [probability/impact]
- **Recommendation**: Adopt/Investigate/Defer/Avoid
- **Rationale**: [trade-offs]
- **Success Criteria**: [baseline] → [target] (measure: [method])
- **Limitations**: NOT for [condition]; [counterargument]

**Action**: 
- **Immediate (0-2wk)**: [actions] (Owner: [role])
- **Short-term (2wk-2mo)**: [actions] (Owner: [role])

[n#]: [URL]
```

## Glossary

**CISA KEV**: Known Exploited Vulnerabilities catalog. Lists CVEs with active exploitation requiring priority patching.

**CVE**: Common Vulnerabilities and Exposures. Standardized security vulnerability ID (e.g., CVE-2024-12345). Scored 0-10 via CVSS.

**Decision criticality**: News blocking decisions, creating material risk, impacting ≥2 roles, time-sensitive (1-6mo), or quantified impact.

**Primary sources**: Original announcements (vendor blogs, CVE DB, official docs) vs secondary reporting (news articles).

**Quantified metrics**: Measurable values with units ("latency <200ms", "$5K/mo") vs vague qualifiers ("fast", "cheap").
