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

**Problem**: Engineering teams lack time-efficient, decision-focused technical news filtering, causing missed critical security/infrastructure updates or information overload.

**Task**: Generate 4-6 decision-critical Q&As from infrastructure and security news.

**Constraints**: Bi-weekly cadence, 2-week validity, primary sources only

**Freshness**: Security/Infrastructure/Releases (≥80% <1mo, 100% <4mo); Standards/Practices (≥70% <2mo, 100% <6mo)

**Decision Criticality** (≥1 required):
1. Blocks infrastructure/security decisions
2. Material risk (breach, outage, compliance)
3. Impacts ≥2 roles
4. Time-sensitive (1-6mo window)
5. Quantified impact (metrics with units)

## Scope

**Audience**: Architects, DevOps/SRE, Security Engineers, Developers, Engineering Managers

**Include**: Security (CVEs, data privacy compliance—GDPR, CCPA, SOC2), Infrastructure/Cloud, Releases, Standards/Regulations, Practices, Ecosystem/Integration

**Exclude**: Marketing, rumors, speculation, stale (>4mo security, >6mo practices)

**Relevance** (≥2 required): Recency (<1mo security, <2mo practices), Multi-phase (≥2), Multi-role (≥2), Time-sensitive (1-6mo), Quantified (metrics+units)

## Requirements

**Structure**: 4-6 Q&As, 150-200 words each, URLs cited

**Phases**: Architecture & Design, Development, Deploy & Release, Operations & Observability

**Priority**: 
1. Critical: Security (CVEs), Infrastructure (cloud, networking)
2. Important: Practices (DevOps, SRE), Releases (breaking changes)
3. Optional: Ecosystem (adoption <5%)

**Coverage**: Roles ≥5, News ≥4 (N#), Visuals (≥2 diagrams, ≥1 table)

**References**: G# (Glossary), N# (News), T# (Tools), S# (Standards), R# (Reports), A# (Citations)

## Execution

### 1. News Discovery & Curation

**Search** (≥10 candidates; prioritize 1-7d security/infrastructure):
- Security: CVE DB, CISA KEV, vendor advisories, GitHub Security
- Infrastructure: AWS/GCP/Azure blogs, K8s blog, CNCF
- Practices: InfoQ, Martin Fowler, SRE Weekly
- Releases: GitHub releases, vendor blogs, registries

**Filter**: Primary sources, meet freshness+criticality, quantified details, balanced categories

**Allocate**: Distribute 4-6 Q&As across phases/categories/roles; record date (YYYY-MM-DD)

### 2. Build References

**Format**:
- G#: term, definition+analogy (used terms only)
- N#: title, source, YYYY-MM-DD, category, URL
- T#: name, description, version, URL
- S#: ID, title, changes, URL
- R#: title, firm, date, findings, URL
- A#: APA 7th with URL

**Citation**: [Ref: N#][n#] inline → [n#]: URL at end; flag uncertainties ("estimated")

### 3. Generate Q&A

**Question**: "[News] implications for [Phase]+[Roles]?" or "[CVE/Change]: response strategy?"

**Avoid**: Generic, hype, unattributed claims, speculation

**Structure** (150-200 words):
1. News: What, when, why, category [Ref: N#][n#]
2. Impact: ≥2 phases, quantified metrics
3. Stakeholders: ≥2 roles, concerns, actions
4. Decision:
   - Alternatives: ≥2 options (cost $, benefit metric, risk probability/impact)
   - Recommendation: Adopt/Investigate/Defer/Avoid + rationale
   - Success Criteria: baseline → target, measurement
   - Limitations: When NOT to use, counterarguments
5. Action: Immediate (0-2wk), short-term (2wk-2mo), owners
6. Links: [n#]: URL

### 4. Add Visuals (Inline Placement)

**Principle**: Embed visuals immediately after relevant text to avoid reader navigation.

**Placement Logic**:
- **Decision comparisons** (≥2 alternatives): Table directly after Decision text
- **Process flows** (impact chains, deployment sequences): Diagram directly after describing the flow
- **Risk/priority matrices**: Diagram inline where risk assessment occurs
- **Metric dashboards**: Table inline with Impact section

**Minimum**: ≥2 diagrams (Mermaid) + ≥1 table, all placed inline within Q&A sections (not grouped separately)

### 5. Validate & Submit

**Check**: Completeness (N≥4, 5+ roles, 4-6 Q&As, 150-200w, URLs, ≥2 diagrams, ≥1 table), Quality (freshness, ≥1 criticality/Q&A, quantified, no hype), Decisions (≥2 alternatives cost/benefit/risk, recommendation+rationale, baseline→target, limitations), Accuracy (verified, contradictions checked, uncertainties flagged)

**Submit**: Glossary (used only), TOC, generation date, expiry (+2wk)

## Validation Checklist

| Check | Criteria | Status |
|-------|----------|--------|
| Freshness | Sec/Infra ≥80% <1mo; Stds/Prac ≥70% <2mo | ☐ |
| References | N≥4 primary sources | ☐ |
| Q&As | 4-6 total, 150-200w each | ☐ |
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
- ✅ "CVE-2024-XXXX (CVSS 9.8): patching strategy?"
- ✅ "K8s 1.30 deprecations: migration approach?"
- ✅ "AWS pricing +20%: cost impact?"

**Bad**: Generic, educational, no trigger
- ❌ "How do CVEs work?"
- ❌ "What is SRE?"
- ❌ "Should we use Kubernetes?"

## Output Format

Single Markdown document with sections: **TOC** → **Executive Summary** → **Phase Overview** → **Q&As** → **References** → **Validation**

### Executive Summary

**Domain**: TechOps | **Period**: YYYY-MM-DD to YYYY-MM-DD | **Coverage**: X Q&As, Y phases

**Key Insights** (top 1-2): News + quantified impact + recommendation + timeline

**Dashboard**:
| Phase | News | Decision | Timeline |
|-------|------|----------|----------|
| [Phase] | [Item] | [Adopt/Defer] | [Xmo] |

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
- [Phase 1]: [metric+unit] (latency +50ms, cost +$2K/mo, CVSS 9.8)
- [Phase 2]: [metric+unit]

```mermaid
[Optional: Process flow diagram if describing deployment/impact sequence]
```

| Metric | Baseline | Target | Timeline |
|--------|----------|--------|----------|
| [Optional: Metrics table if ≥3 quantified impacts] | | | |

**Stakeholders**: 
- [Role 1]: [concern] → [action]
- [Role 2]: [concern] → [action]

**Decision**: 
- Alternatives: 
  - A: [description] | Cost: $ | Benefit: [metric] | Risk: [probability/impact]
  - B: [description] | Cost: $ | Benefit: [metric] | Risk: [probability/impact]
- Recommendation: Adopt/Investigate/Defer/Avoid
- Rationale: [trade-offs]
- Success Criteria: [baseline] → [target] (measure: [method])
- Limitations: NOT for [condition]; [counterargument]

| Option | Cost | Benefit | Risk | Timeline |
|--------|------|---------|------|----------|
| A | [$] | [metric] | [prob/impact] | [Xwk] |
| B | [$] | [metric] | [prob/impact] | [Xwk] |

**Action**: 
- Immediate (0-2wk): [actions] (Owner: [role])
- Short-term (2wk-2mo): [actions] (Owner: [role])

```mermaid
[Optional: Timeline/deployment diagram if showing action sequence]
```

[n#]: [URL]
```

## Glossary

**CISA KEV**: Known Exploited Vulnerabilities catalog; CVEs with active exploitation requiring priority patching.

**CVE**: Common Vulnerabilities and Exposures; standardized ID (e.g., CVE-2024-12345), CVSS-scored 0-10.

**Decision criticality**: Blocks decisions, material risk, ≥2 roles impact, time-sensitive (1-6mo), quantified impact.

**Primary sources**: Original announcements (vendor blogs, CVE DB, official docs) vs secondary (news articles).

**Quantified metrics**: Values with units ("latency <200ms", "$5K/mo") vs vague ("fast", "cheap").
