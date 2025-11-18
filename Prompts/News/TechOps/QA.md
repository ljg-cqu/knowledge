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

Generate 4-6 decision-critical Q&As from recent infrastructure and security news for engineering teams.

**Goal**: Enable informed technical decisions via minimal viable news tracking.

**Cadence**: Bi-weekly | **Validity**: 2 weeks

**Freshness Thresholds**:
- Security/Infrastructure/Releases: ≥80% <1mo, 100% <4mo
- Standards/Practices: ≥70% <2mo, 100% <6mo

**Decision Criticality** (≥1 per Q&A):
1. Blocks infrastructure/security decisions
2. Creates material risk/threat
3. Impacts ≥2 roles
4. Requires action within 1-6mo
5. Has quantified impact

## Scope

**Audience**: Architects, DevOps/SRE, Security Engineers, Developers, Engineering Managers

**Include**: Security (CVEs), infrastructure, releases, ecosystem, standards, practices, benchmarks

**Exclude**: Marketing, rumors, speculation, stale news (>4mo for security)

**Categories**: Technical Releases, Infrastructure/Cloud, Security, Ecosystem/Integration, Standards/Regulations, Engineering Practices

**Relevance** (≥2 required): Recency, multi-phase impact, multi-role impact, time-sensitive (1-6mo), quantified metrics

## Requirements

**Q&A Structure**: 4-6 total | 120-200 words each | cited sources with URLs

**Lifecycle Phases**: Architecture & Design, Development, Deploy & Release, Operations & Observability

**Topic Coverage** (Priority order):
1. **Critical**: Security (CVEs, vulnerabilities), infrastructure (cloud, networking)
2. **Important**: Practices (DevOps, SRE), major releases
3. **Optional**: Ecosystem updates (<5% adoption impact)

**Stakeholder Coverage**: Address ≥5 distinct roles across all Q&As

**References**: Glossary (terms used), News sources (≥4), Tools, Standards, Reports, Citations

**Visuals**: ≥2 diagrams + ≥1 table

**Quality Validation**: See [Validation Checklist](#validation-checklist) for complete criteria

## Execution

### 1. News Discovery & Curation

**Search** (≥10 candidates, prioritize 1-7d for security/infrastructure):
- **Security**: CVE DB, CISA, vendor advisories, GitHub
- **Infrastructure**: Cloud blogs, Kubernetes, registries
- **Practices**: InfoQ, Martin Fowler, SRE Weekly
- **Releases**: GitHub, vendor blogs

**Curate**:
- Prefer primary sources (official vendor announcements, CVE databases, official blogs vs secondary reporting)
- Meet freshness thresholds and ≥1 criticality criterion
- Include specific, quantified details
- Balance across categories

**Allocate**: Distribute 4-6 Q&As across phases, categories, and roles. Record generation date (YYYY-MM-DD).

### 2. Build References

**Reference Types**:
- **G#**: Glossary (term, definition with analogy, context) - only terms used
- **N#**: News (title, source, date, category, URL)
- **T#**: Tools (name, description, version, URL)
- **S#**: Standards (ID, title, key changes, URL)
- **R#**: Reports (title, firm, date, findings, URL)
- **A#**: Citations (APA 7th format with URL)

**Citation Format**: [Ref: N#][n#] in text → [n#]: URL at end

**Evidence**: Prefer primary sources; label uncertainties when present

### 3. Generate Q&A

**Question Patterns**: 
- "[News] implications for [Phase]+[Roles]?"
- "[CVE/Change]: response strategy?"
- "[Release/Change]: adoption approach?"

**Avoid**: Generic questions, hype, unattributed claims, speculation

**Structure** (120-200 words total):
1. **News**: What, when, why, category [Ref: N#][n#]
2. **Impact**: ≥2 phases with quantified metrics (performance/reliability/security/cost)
3. **Stakeholders**: ≥2 roles with specific concerns and actions
4. **Decision**: 
   - Compare ≥2 alternatives (costs, benefits, risks)
   - Recommendation (Adopt/Investigate/Defer/Avoid) + rationale
   - Success criteria + limitations/counterarguments
5. **Action**: Immediate (0-2wk) and short-term (2wk-2mo) steps with owners
6. **Links**: [n#]: URL

**Self-Check**: Per [Validation Checklist](#validation-checklist)

### 4. Add Visuals

Include ≥2 diagrams (Mermaid flows/matrices) + ≥1 table

### 5. Validate & Submit

**Validate**:
- References, coverage, citations, word count, visuals per requirements
- Fresh news (no hype/speculation), criticality met, impact quantified
- Recommendations with rationale + alternatives + limitations, diverse sources, valid URLs
- Self-review: verify facts against authoritative sources, check contradictions, flag uncertainties

**Submit**: Include complete glossary, TOC, generation date, and expiry date (generation + 2 weeks)

## Validation Checklist

| Check | Criteria | Status |
|-------|----------|--------|
| Freshness | Sec/Infra ≥80% <1mo; Stds/Prac ≥70% <2mo | PASS/FAIL |
| References | Adequate coverage (N≥4, others as needed) | PASS/FAIL |
| Q&As | 4-6 total, 120-200w each | PASS/FAIL |
| Coverage | Security and infrastructure emphasized | PASS/FAIL |
| Roles | ≥5 distinct roles covered | PASS/FAIL |
| Criticality | All meet ≥1 criterion | PASS/FAIL |
| Impact | All with ≥2 phases+roles, quantified | PASS/FAIL |
| Decision | All with alternatives+recommendation+rationale+limitations | PASS/FAIL |
| Citations | All Q&As cited with valid URLs | PASS/FAIL |
| Verification | Facts verified, contradictions checked, uncertainties flagged | PASS/FAIL |
| Visuals | ≥2 diagrams, ≥1 table | PASS/FAIL |
| Dates | Generation: ___ | Expiry: ___ (+2wk) | INFO |

## Question Quality

**Good Examples**:
- "CVE-2024-XXXX critical vulnerability: What's our patching strategy?"
- "Kubernetes 1.30 deprecations: How to migrate affected workloads?"
- "AWS pricing changes: What's the cost impact for our infrastructure?"

**Bad Examples** (avoid):
- "How do CVEs work?" (generic, not news-driven)
- "What is SRE?" (educational, not decision-focused)
- "Should we use Kubernetes?" (no specific news trigger)
- Feature announcements without decision impact

## Output Format

Single Markdown document with sections: **TOC** → **Executive Summary** → **Phase Overview** → **Q&As** → **References** → **Validation**

### Executive Summary

Include:
- Domain, period, coverage summary
- 1-2 key insights: high-impact decisions with news, impact, recommendation, timeline
- Dashboard table: Phase | News | Decision | Timeline
- Role and reference counts

### Phase Overview Table

| Phase | Categories | Top News | Roles |
|-------|------------|----------|-------|
| Architecture & Design | Security, Infrastructure | [Item] | Architect, SRE |
| Development | Practices, Releases | [Item] | Developer, DevOps |
| Deploy & Release | Infrastructure, Security | [Item] | DevOps, SRE |
| Operations & Observability | Infrastructure, Practices | [Item] | SRE, Manager |

### Q&A Template

```
### Q#: [News Question + Phase + Roles]

**Phase**: [Phase] | **Roles**: [Primary, Secondary] | **Category**: [Type] | **Criticality**: [Criterion]

**News**: What happened, when, why it matters [Ref: N#][n#]

**Impact**: Quantified metrics across ≥2 phases (performance/reliability/security/cost)

**Stakeholders**: 
- **[Role]**: Concerns and required actions

**Decision**: 
- **Alternatives**: [Option A] vs [Option B] (costs, benefits, risks)
- **Recommendation**: Adopt/Investigate/Defer/Avoid
- **Rationale**: Trade-offs analysis
- **Success Criteria**: Measurable targets
- **Limitations**: When NOT recommended; counterarguments

**Action**: 
- **Immediate (0-2wk)**: [Actions] (Owner: [Role])
- **Short-term (2wk-2mo)**: [Actions] (Owner: [Role])

[n#]: URL
```

## Glossary

**MECE** (Mutually Exclusive, Collectively Exhaustive): Framework ensuring sections are distinct with no gaps or overlaps. Like organizing files into folders where each file belongs to exactly one folder, and all files are covered.

**Primary sources**: Original announcements or data (e.g., vendor blogs, CVE databases, official docs) vs secondary reporting (e.g., news articles summarizing announcements).

**APA 7th format**: Author, A. A. (Year). Title. Source. URL (e.g., Smith, J. (2024). Cloud security practices. AWS Blog. https://aws.amazon.com/blogs/...)

**Quantified metrics**: Specific, measurable values with units (e.g., "latency <200ms", "cost $5K/mo", "error rate <0.1%") vs vague qualifiers ("fast", "cheap", "reliable").

**Decision criticality**: News that blocks decisions, creates material risk, impacts ≥2 roles, requires action within 1-6mo, or has quantified impact.
