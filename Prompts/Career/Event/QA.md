# Event Analysis Framework

Generate evidence-based analyses of major incidents with root cause investigation, multi-perspective evaluation, and transferable lessons.

---

## Definition

**Purpose**: Document, analyze, extract lessons from significant events across technology, business, security, regulatory domains

**Output**: 20–30 analyses (300–600w) | 6 domains (3–5 each) | Basic:Intermediate:Advanced 20:40:40% (±5pp) | EN 50–70%, ZH 20–40%, Other 5–15%

**Requirements**: Timestamped timeline, RCA (proximate + systemic), quantified impact, multi-perspective (≥60% with 3+ views), actionable lessons, ≥3 citations/analysis (≥5 for 40%)

**Constraints**: Primary sources ≥80% (incident reports, official statements, forensics, filings); ≥60% contemporary (±2yr); all links accessible/archived

**Source Quality**: Official Reports/Post-mortems > Academic Research > Government Docs > Industry Analysis > News Archives > Commentary

**Assumptions**: Events have verifiable facts; multiple interpretations exist; cross-domain patterns transferable

---

## Terminology

| Term | Definition |
|------|------------|
| **RCA** | Root Cause Analysis—systematic investigation identifying fundamental failure sources (proximate + systemic) |
| **MTTR/MTBF** | Mean Time To Repair / Between Failures—system reliability metrics |
| **CVE** | Common Vulnerabilities and Exposures—standardized security flaw identifiers |
| **Zero-day** | Exploited vulnerability unknown to vendor or lacking available patch |
| **APT** | Advanced Persistent Threat—sophisticated, sustained intrusion campaign (typically nation-state) |
| **DDoS** | Distributed Denial of Service—coordinated traffic flood overwhelming target systems |
| **Ransomware** | Malware encrypting data to extort payment for decryption keys |
| **Supply Chain Attack** | Compromise via trusted third-party dependencies, libraries, or vendors |
| **Post-mortem** | After-action analysis documenting incident timeline, causes, impact, and remediation |
| **SLA** | Service Level Agreement—contractual performance guarantees with penalties for breach |

---

## Domains (MECE)

| Domain | Scope | Examples |
|--------|-------|----------|
| **Security** | Breaches, attacks, vulnerabilities, data leaks | Equifax 2017, SolarWinds 2020, Log4Shell 2021 |
| **Technical** | Outages, system failures, infrastructure issues | AWS S3 2017, Facebook BGP 2021, Knight Capital 2012 |
| **Market** | Crashes, bubbles, disruptions, liquidity shocks | 2008 Financial Crisis, FTX 2022, GameStop 2021 |
| **Regulatory** | Policy changes, enforcement, compliance failures | GDPR 2018, Cambridge Analytica 2018, Theranos 2018 |
| **Business** | Scandals, recalls, governance failures, fraud | Boeing 737 MAX, VW Dieselgate, Wells Fargo |
| **Technology** | Platform changes, deprecations, ecosystem shifts | Flash EOL 2020, Twitter API changes, Apple ATT |

---

## Complexity Levels

| Level | % | Focus | Perspectives | Evidence | Core Elements |
|-------|---|-------|--------------|----------|---------------|
| **Basic** | 20±5 | Single clear cause, linear timeline | 1–2 | Documented facts | Timeline, 1 RCA method, impact metrics, 3 citations, 1 lesson |
| **Intermediate** | 40±5 | Multiple causes, interconnected factors | 2–3 cross-domain | Causal chains | Detailed timeline, 2 RCA methods, technical + business views, 5+ citations, 3 lessons |
| **Advanced** | 40±5 | Systemic causes, cascading failures | 4+ industry-wide | Deep forensics + context | Complete reconstruction, 3+ RCA methods, multi-level impact, alternatives, 8+ citations, 5+ lessons, prevention framework |

---

## Structure (per Analysis)

1. **Overview** (2–3 sent): What, when, who affected [Ref: ID]
2. **Timeline** (5–10 points): Chronology with timestamps, critical decision points [Ref: ID]
3. **Root Cause** (4–6 sent): Proximate causes, contributing factors, systemic issues with causal chains [Ref: ID]
4. **Technical** (3–5 sent): Mechanisms, vulnerabilities, attack vectors, failure modes [Ref: ID]
5. **Impact** (3–4 sent): Quantified damage—financial, operational, reputational, regulatory [Ref: ID]
6. **Response** (Int/Adv, 3–4 sent): Actions taken, resolution timeline, effectiveness [Ref: ID]
7. **Perspectives** (Int/Adv, 4–6 sent): Technical, business, regulatory, public views with evidence [Ref: ID]
8. **Lessons** (4–6 sent): Transferable insights, prevention strategies, detection improvements [Ref: ID]
9. **Alternatives** (Adv, 2–3 sent): Counterfactual scenarios with estimated outcomes
10. **Takeaway**: Actionable, non-obvious, transferable, falsifiable insight

---

## Process

### 1. Build References (BEFORE Analysis)

| Type | Floor | Elements | Format |
|------|-------|----------|--------|
| **Glossary** | ≥15 | Technical terms, acronyms, methodologies | G#. Term \| Definition \| Detection/Prevention |
| **Tools** | ≥8 | Analysis tools, incident response platforms | T#. Name \| Function \| Deployment \| Limitations \| URL |
| **Literature** | ≥8 | Frameworks, methodologies, research | L#. Author (Year) \| Title \| Core Frameworks |
| **Citations** | ≥20 | Event sources with diversity | Full citation \| Type \| [EN/ZH/Other] \| URL |

**Diversity Requirements**: ≥4 source types; no single source >20%; prioritize official reports

### 2. Event Selection

**Process**: Select 5–6 domains → Identify 3–5 events each (20–30 total) → Assign Basic:Int:Adv 20:40:40 (±5pp) → Ensure temporal, geographic, domain diversity

**Criteria**: Significant quantified impact, documented evidence from primary sources, transferable lessons, multi-perspective analysis possible

### 3. Analysis Generation

**Process**: Follow 10-part structure | Cite [Ref: ID] inline | Build causal chains | Analyze alternative scenarios | Quantify all impacts

**Checkpoint** (per 3 analyses): Word count 300–600, timeline accuracy verified, citation requirements met, lessons actionable, perspectives documented

### 4. Create Artifacts

**Per domain**: ≥1 timeline diagram + ≥1 impact table (attack chains, decision trees, cascade diagrams)

### 5. Validation

Run 18-check validation. **ALL PASS required**. FAIL → fix → re-validate ALL

---

## Verification Standards

**Cross-check**: Verify statistics, frameworks, claims against ≥2 authoritative sources  
**Uncertainty**: Flag with qualifiers ("estimated," "reported"); cite confidence levels where available  
**Conflicts**: Present competing narratives with citations for each perspective  
**Outdated Info**: Note if findings superseded by later investigations

**Authoritative Source** (≥1): Peer-reviewed publication | Senior practitioner (10+ years) | Framework originator | Data-backed with disclosed methodology | Industry standard body

---

## Validation Checklist (ALL PASS Required)

| # | Check | Criteria | Purpose |
|---|-------|----------|---------|
| 1 | Reference counts | G≥15, T≥8, L≥8, A≥20 | Sufficient evidence base |
| 2 | Event counts | 20–30 total; Basic:Int:Adv 20:40:40 (±5pp) | Balanced scope & depth |
| 3 | Citations per analysis | ≥80% have ≥3 [Ref]; ≥40% have ≥5 | Evidence depth |
| 4 | Language distribution | EN 50–70%, ZH 20–40%, Other 5–15% | Geographic diversity |
| 5 | Contemporary sources | ≥60% from event period ±2yr | Historical accuracy |
| 6 | Source diversity | ≥4 types; no single >20% | Bias mitigation |
| 7 | Link validation | 100% functional or archived | Verifiability |
| 8 | Cross-reference integrity | All [Ref: ID] resolve correctly | No broken citations |
| 9 | Word count compliance | Sample 5: all within 300–600 | Consistent depth |
| 10 | Takeaway quality | All actionable, non-obvious, transferable | High-value insights |
| 11 | Per-domain rigor | Each: ≥3 official sources + complete timeline | Analytical rigor |
| 12 | Timeline verification | All events have verified chronology with sources | Factual accuracy |
| 13 | RCA depth | ≥70% identify both systemic + proximate causes | Root cause clarity |
| 14 | Fact-checking | Sample 5: cross-validated against primary sources | Error detection |
| 15 | Multi-perspective | ≥60% include 3+ distinct viewpoints with evidence | Balanced analysis |
| 16 | Impact quantification | ≥80% include specific damage metrics (financial, users, etc.) | Concrete assessment |
| 17 | Artifact completeness | Each domain: ≥1 timeline + ≥1 table/diagram | Visual clarity |
| 18 | TOC functionality | Present with working section links | Navigation |

**Result**: ✅ ALL PASS → deliver | ❌ ANY FAIL → list failures → fix → re-validate ALL

---

## Multi-Perspective Framework

**Required Viewpoints** (select ≥3 per analysis):
- **Technical vs. Business**: Implementation details vs. strategic/financial impact
- **Prevention vs. Response**: Proactive controls vs. reactive incident handling
- **Individual vs. Systemic**: Human error vs. organizational/cultural factors
- **Short-term vs. Long-term**: Immediate damage vs. sustained consequences
- **Internal vs. External**: Organizational perspective vs. industry/public view
- **Victim vs. Attacker/Competitor**: Defensive vs. offensive/competitive analysis

**Analysis Requirements**:
- 2+ distinct causal interpretations with evidence [Ref: ID]
- Alternative scenarios with estimated impact differences
- Evidence limitations explicitly noted [Ref: ID]
- Conflicting narratives presented with sources
- Quantified uncertainties where data incomplete

**Insight Quality**:
- ✅ **Good**: "Supply chain attacks exploit trust relationships more than technical vulnerabilities; defense requires architectural assumptions rethinking and build pipeline verification"
- ❌ **Poor**: "Security is important and organizations should invest in it" (vague, obvious, not actionable)

---

## Common Pitfalls & Solutions

| Category | ❌ Avoid | ✅ Instead |
|----------|----------|------------|
| **Selection** | Obscure events lacking sources | Significant, well-documented with multiple primary sources |
| | Single domain concentration | Balanced cross-domain coverage (6 domains, 3–5 each) |
| | Recent events only | Temporal diversity (mix of historical and recent) |
| | Western-centric only | Geographic diversity across regions |
| **Analysis** | Missing or vague timeline | Detailed chronology with specific timestamps and sources |
| | Single cause attribution | Proximate + contributing + systemic causes with causal chains |
| | Vague impact statements | Quantified metrics (financial losses, users affected, downtime) |
| | Technical perspective only | Multi-perspective with ≥3 distinct viewpoints |
| | Missing or generic citations | Heavily cited with specific [Ref: ID] to authoritative sources |
| | Hindsight bias | Focus on information available at decision time |
| | Obvious or generic lessons | Non-obvious, actionable, transferable insights |
| **Quality** | Low-quality sources | Primary sources (reports, forensics, official statements) |
| | Broken links | All URLs accessible or archived |
| | Incomplete references | All [Ref: ID] resolve to complete citation |

---

## Examples

### Basic (320w): Cloudflare BGP Route Leak (June 24, 2019)

**Complexity**: Basic | **Domain**: Technical Failures

**Overview**: Cloudflare suffered global outage affecting millions of websites for 30 minutes due to configuration error during routine maintenance [Ref: A1].

**Timeline**:  
- **13:42 UTC** - WAF rule deployment begins  
- **13:55** - CPU spike to 100% across global network  
- **14:00** - Services completely offline  
- **14:07** - Root cause identified (regex backtracking)  
- **14:12** - Rollback completed  
- **14:20** - Full service recovery [Ref: A1]

**Root Cause**: Regex optimization in WAF rules caused catastrophic backtracking on legitimate traffic patterns, consuming all CPU. Single problematic expression: `.*(?:.*=.*){  }` with repeated nested quantifiers [Ref: A1, G1]. **Proximate**: Untested regex deployed to production. **Systemic**: Insufficient load testing for adversarial edge cases; deployment without canary rollout or gradual traffic ramping [Ref: A1].

**Technical**: PCRE regex engine's exponential time complexity when processing crafted input patterns [Ref: A1]. CPU exhaustion prevented all request processing. Global synchronized deployment amplified impact across all data centers simultaneously [Ref: A1].

**Impact**: 50% of HTTP requests failed globally; ~27 minutes total downtime; millions of customer sites affected; no data breach or loss. Estimated $20M+ lost revenue across customer base [Ref: A2]. Significant reputational damage despite quick resolution.

**Response**: Immediate rollback within 12 minutes of identification. Post-incident: implemented ReDoS (Regular Expression Denial of Service) detection in CI/CD pipeline, mandatory canary deployments for configuration changes, CPU-based automated kill switches [Ref: A1].

**Lessons**:  
1. Regex complexity poses security and availability risk requiring automated analysis [Ref: A3]
2. Gradual rollouts essential even for "safe" configuration changes
3. Automated kill switches prevent single failures from cascading globally

**Takeaway**: Configuration changes carry equal risk to code deployments; testing must include adversarial inputs and performance limit validation, not just functional correctness.

---

### Intermediate (420w): Equifax Data Breach (March–July 2017)

**Complexity**: Intermediate | **Domain**: Security

**Overview**: Equifax exposed 147.9M people's sensitive data through unpatched Apache Struts vulnerability (CVE-2017-5638), compounded by multiple security control failures and 2-month delayed detection [Ref: A4, A5].

**Timeline**:  
- **Mar 7** - CVE-2017-5638 published; patch available  
- **Mar 8** - DHS alerts Equifax to vulnerability  
- **Mar 9** - Equifax patches "some systems," misses ACIS application  
- **Mar 10–May 13** - Attackers access systems undetected (66 days)  
- **May 13** - Suspicious traffic detected  
- **Jul 29** - Breach scope fully confirmed  
- **Sep 7** - Public disclosure (6 months post-initial compromise) [Ref: A4, A5]

**Root Cause**:  
**Proximate**: Unpatched CVE-2017-5638 allowing remote code execution via Content-Type header [Ref: A4].  
**Contributing**: (1) Expired SSL certificate blocked vulnerability scanning of ACIS [Ref: A6], (2) Network segmentation failures enabled lateral movement, (3) Plaintext credentials stored in files, (4) No file integrity monitoring detected data exfiltration.  
**Systemic**: Fragmented IT oversight across 50+ business units; no centralized patch management; expired asset inventory; security deprioritized culturally [Ref: A8].

**Technical**: Attackers exploited Jakarta Multipart parser deserialization flaw in Content-Type header, deployed web shells for persistence, extracted 48 databases via encrypted channels mimicking normal traffic patterns [Ref: A4, A5]. Lateral movement enabled by flat network architecture.

**Impact**: 147.9M consumer records (SSN, DOB, addresses); 209K credit cards; 182K dispute documents. $1.4B settlement; $1.5B+ total costs including forensics, remediation, legal [Ref: A6]. CEO, CIO, CSO resigned. Stock dropped 35% (-$5B market cap). Congressional hearings; criminal charges against executives trading on insider knowledge.

**Perspectives**:  
- **Technical**: Entirely preventable with basic security hygiene; defense-in-depth absent [Ref: A7]  
- **Business**: Culture prioritized revenue growth over security investment; security seen as cost center [Ref: A8]  
- **Regulatory**: Catalyzed stricter data breach notification laws; increased FTC/CFPB oversight [Ref: A9]  
- **Public**: Widespread trust erosion in credit bureaus; calls for regulation of credit reporting industry [Ref: A10]

**Response**: 66 days to detect; 6 additional weeks to disclose publicly. Launched TrustedID monitoring (criticized for arbitration clauses). Implemented full-disk encryption, micro-segmentation, 24/7 SOC monitoring [Ref: A6].

**Lessons**:  
1. Patch management is existential for companies holding sensitive data  
2. Defense-in-depth (segmentation, encryption, monitoring) prevents total compromise from single vulnerability  
3. Monitoring must detect lateral movement and anomalous data access, not just perimeter breaches  
4. Timely disclosure is both ethical imperative and legal requirement

**Takeaway**: Security incidents rarely stem from single cause; organizational culture and basic security hygiene matter more than sophisticated defenses when fundamentals are absent.

---

### Advanced (580w): SolarWinds Supply Chain Attack (March–Dec 2020)

**Complexity**: Advanced | **Domain**: Security, Business

**Overview**: Russian APT29 (Cozy Bear) compromised SolarWinds Orion platform via malicious code injection into build process, affecting 18,000+ organizations including nine U.S. federal agencies, demonstrating sophisticated supply chain attack at unprecedented scale [Ref: A11, A12, A13].

**Timeline**:  
- **Sep 2019** - Target reconnaissance begins  
- **Oct 2019–Feb 2020** - C2 infrastructure preparation  
- **Mar 2020** - SUNBURST backdoor inserted into Orion source  
- **Mar 26, 2020** - Malicious update 2019.4 HF 5 signed and released  
- **Apr–May 2020** - Selective implant activation (~100 of 18,000 targets)  
- **Jun–Nov 2020** - Sustained stealthy exfiltration from high-value targets  
- **Dec 8, 2020** - FireEye discloses own breach, discovers SUNBURST  
- **Dec 13, 2020** - SolarWinds confirms compromise  
- **Dec 2020–Jan 2021** - Industry-wide emergency response and investigation  
- **2021–ongoing** - Attribution confirmed, forensics, long-term remediation [Ref: A11, A12]

**Root Cause**:  
**Attack Chain**: (1) Compromise build environment access controls, (2) Inject SUNBURST backdoor into Orion platform DLLs, (3) Sign with legitimate SolarWinds certificate, (4) Deploy via trusted automatic update mechanism, (5) Selectively activate implants (0.2% of victims), (6) Deploy second-stage TEARDROP/RAINDROP for high-value targets, (7) Establish C2 via legitimate cloud infrastructure (GoDaddy, AWS) [Ref: A12, A13].  
**Proximate**: Weak build system access controls; insufficient code review for build output differences; lack of build integrity verification [Ref: A14].  
**Systemic**: (1) Software supply chain fundamentally lacks verifiable trust mechanisms, (2) Security monitoring focuses on perimeter, not trusted software behavior, (3) Attribution delays enabled 9+ months undetected access, (4) Interconnected IT infrastructure creates systemic single points of failure.

**Technical**: SUNBURST used domain generation algorithm (DGA) for C2 via DNS queries, mimicked normal Orion "Orion Improvement Program" traffic patterns, delayed execution 12–14 days to evade sandboxes, employed blocklisting of security researcher IP ranges and forensic tools. Code injection via MSBuild project configuration modification [Ref: A12, A15]. Second-stage focused on <100 high-value targets with custom tooling avoiding automated detection.

**Impact**:  
- **Direct**: 18,000+ organizations installed backdoor; ~100 actively exploited with sustained access  
- **Government**: Nine federal agencies (Treasury, State, Commerce, Homeland Security, DOE, DOD, Justice, NIH, NNSA) [Ref: A16]  
- **Private Sector**: Microsoft, FireEye, Cisco, Intel, Deloitte, VMware  
- **Financial**: SolarWinds $18M immediate costs + ongoing litigation; industry-wide estimated $100B+ remediation [Ref: A17]  
- **Strategic**: Exposed critical U.S. cyber defense capability gaps; compromised sensitive communications; prompted Executive Order 14028 on cybersecurity

**Perspectives**:  
- **Technical**: Highlighted systematic neglect of build system security as critical attack surface [Ref: A14]  
- **Intelligence**: Attribution took months despite advanced capabilities; Russia denied involvement; exposed intelligence community's detection gaps [Ref: A16]  
- **Regulatory**: Accelerated zero-trust architecture mandates, software bill of materials (SBOM) requirements, secure software development attestations [Ref: A18]  
- **Industry**: Fundamental trust crisis in software supply chain; recognition that perimeter security insufficient [Ref: A19]  
- **Geopolitical**: Cyber espionage elevated to tier-one national security threat; diplomatic sanctions imposed

**Response**: Nine months undetected; detection by victim (FireEye) not SolarWinds monitoring. Massive coordinated industry response: emergency patches, forensic investigations, infrastructure hardening. Government response: diplomatic sanctions, Executive Order 14028, CISA emergency directives, increased funding for cyber defense [Ref: A18].

**Alternative Scenarios**:  
- **If detected at build stage**: Attack prevented entirely; estimated $100B+ damage avoided  
- **If SBOM mandated**: Faster anomaly detection via dependency/hash verification  
- **If zero-trust architecture implemented**: Limited lateral movement; reduced high-value target compromise  
- **If behavioral monitoring of trusted software**: Earlier detection of anomalous SUNBURST C2 patterns

**Preventive Framework**:  
1. **Build System Isolation**: Air-gapped build environments, hardware-backed code signing, comprehensive build audit logging [Ref: A14]  
2. **Code Signing Integrity**: Hardware security modules (HSMs) for private keys, multi-party approval for signing  
3. **Transparency**: Software Bill of Materials (SBOM), reproducible builds, cryptographic build attestations  
4. **Behavioral Analytics**: Monitor trusted software for anomalous behavior (network, file, process patterns)  
5. **Zero-Trust Architecture**: Micro-segmentation, least-privilege access, continuous authentication  
6. **Threat Intelligence Sharing**: Industry-government collaboration, rapid IOC distribution

**Lessons**:  
1. Trust is the fundamental vulnerability in modern software supply chains; verification must replace implicit trust  
2. Sophisticated state actors target weakest infrastructure link (build systems), not strongest (perimeter defenses)  
3. Detection requires monitoring behavior of trusted processes, not just untrusted sources  
4. Response coordination is critical for systemic threats affecting entire industries  
5. Regulatory frameworks persistently lag technical reality; proactive security investment essential  
6. Supply chain security requires rethinking software development and distribution architecture

**Takeaway**: Modern cyber warfare exploits trust relationships rather than purely technical vulnerabilities; supply chain security requires paradigm shift from perimeter defense to cryptographic verification at every layer, with transparency and behavioral monitoring of even trusted components.

---

## Output Structure

```markdown
# Event Analysis Compendium

## Table of Contents
1. Overview & Methodology
2. Event Distribution Summary
3. Domain Analyses
   - 3.1 Security
   - 3.2 Technical
   - 3.3 Market
   - 3.4 Regulatory
   - 3.5 Business
   - 3.6 Technology
4. References
   - 4.1 Glossary
   - 4.2 Tools & Systems
   - 4.3 Literature
   - 4.4 Citations
5. Validation Report

## 1. Overview & Methodology

[Summarize framework, selection criteria, analysis approach]

## 2. Event Distribution Summary

| Domain | Date Range | Count | Basic/Int/Adv | Primary Sources |
|--------|------------|-------|---------------|-----------------|
| Security | [earliest]–[latest] | X | X/X/X | [List 2-3 key sources] |
| Technical | ... | ... | ... | ... |
[Continue for all domains]

## 3. Domain Analyses

### 3.1 Security

#### Event #X: [Event Name] ([Date])

**Complexity**: [Basic/Int/Adv] | **Domain**: Security | **Impact**: [Scale]  
**Takeaway**: [Actionable, non-obvious, transferable, falsifiable]

**Overview**: [What, when, who affected] [Ref: ID]

**Timeline**:  
- **[Timestamp]** - [Event] [Ref: ID]
- **[Timestamp]** - [Event] [Ref: ID]
[5–10 points]

**Root Cause**: [Proximate + contributing + systemic causes with causal chains] [Ref: ID]

**Technical**: [Mechanisms, vulnerabilities, attack vectors, failure modes] [Ref: ID]

**Impact**: [Quantified financial, operational, reputational, regulatory damage] [Ref: ID]

**Response** (Int/Adv): [Actions taken, resolution timeline, effectiveness assessment] [Ref: ID]

**Perspectives** (Int/Adv):  
- **[Viewpoint 1]**: [Analysis with evidence] [Ref: ID]
- **[Viewpoint 2]**: [Analysis with evidence] [Ref: ID]
- **[Viewpoint 3+]**: [Analysis with evidence] [Ref: ID]

**Lessons**: [Numbered list of transferable insights with prevention/detection improvements] [Ref: ID]

**Alternatives** (Adv): [Counterfactual scenarios with estimated outcome differences]

**Artifacts**:
```
[Timeline diagram]
[Impact assessment table/matrix]
```

[Repeat for all events in domain]

[Repeat structure for all 6 domains]

## 4. References

### 4.1 Glossary (≥15 terms)

**G1. Term (Acronym)**: Definition. **Detection/Prevention**: [Methods].  
**G2. ...**: ...  
[Alphabetized]

### 4.2 Tools & Systems (≥8 tools)

**T1. Name**: Description. **Function**: [Purpose]. **Deployment**: [Context]. **Limitations**: [Constraints]. **URL**: [link]  
**T2. ...**: ...  
[Grouped by category]

### 4.3 Literature (≥8 sources)

**L1.** Author, A. A. (Year). *Title*. Publisher/Source. [Core frameworks/topics covered]  
**L2.** ...  
[Grouped by language: EN, then ZH, then Other]

### 4.4 Citations (≥20 sources)

**A1.** [Full APA 7th edition citation]. Type: [Report/Academic/Regulatory/Industry/News]. [EN/ZH/Other]. URL or Archive link  
**A2.** ...  
[Sorted by ID]

## 5. Validation Report

| # | Check | Measurement | Criteria | Status | Notes |
|---|-------|-------------|----------|--------|-------|
| 1 | Reference counts | G:__ T:__ L:__ A:__ | G≥15, T≥8, L≥8, A≥20 | PASS/FAIL | |
| 2 | Event counts | Total:__ (B:__ I:__ A:__) | 20–30; 20/40/40% (±5pp) | PASS/FAIL | |
| 3 | Citations per analysis | __% ≥3; __% ≥5 | ≥80% ≥3; ≥40% ≥5 | PASS/FAIL | |
| 4 | Language distribution | EN:__% ZH:__% Other:__% | 50–70% / 20–40% / 5–15% | PASS/FAIL | |
| 5 | Contemporary sources | __% within ±2yr | ≥60% | PASS/FAIL | |
| 6 | Source diversity | __ types; max __% | ≥4 types; max 20% | PASS/FAIL | |
| 7 | Link validation | __/__  accessible | 100% | PASS/FAIL | |
| 8 | Cross-references | __/__ resolved | 100% | PASS/FAIL | |
| 9 | Word count | Sample 5: __/5 compliant | 100% (300–600w) | PASS/FAIL | |
| 10 | Takeaway quality | __/__ meet standards | 100% actionable+novel | PASS/FAIL | |
| 11 | Per-domain rigor | __/6 complete | Each: ≥3 official + timeline | PASS/FAIL | |
| 12 | Timeline verification | __/__ verified | 100% | PASS/FAIL | |
| 13 | RCA depth | __% systemic+proximate | ≥70% | PASS/FAIL | |
| 14 | Fact-checking | Sample 5: __/5 validated | 100% | PASS/FAIL | |
| 15 | Multi-perspective | __% have 3+ views | ≥60% | PASS/FAIL | |
| 16 | Impact quantification | __% quantified | ≥80% | PASS/FAIL | |
| 17 | Artifacts | __/6 domains complete | Each: ≥1 timeline + ≥1 table | PASS/FAIL | |
| 18 | TOC functionality | Links tested | All functional | PASS/FAIL | |

**Final Status**: ✅ ALL PASS → DELIVER | ❌ FAILED CHECKS → [List] → FIX → RE-VALIDATE ALL
```

---

## Usage Instructions

1. **Collect References** (G≥15, T≥8, L≥8, A≥20) prioritizing official reports and contemporary sources **BEFORE** writing analyses
2. **Select Events**: 20–30 significant events across 6 domains with temporal/geographic diversity; assign Basic:Int:Adv 20:40:40 (±5pp)
3. **Generate Analyses**: Follow 10-part structure; include detailed timelines, multi-method RCA, multi-perspective evaluation; cite heavily
4. **Create Artifacts**: ≥1 timeline diagram + ≥1 impact table/matrix per domain
5. **Validate**: Run 18-check validation—ALL PASS required before delivery
6. **Format Output**: Use structured format with functional TOC, complete references, validation report

**Success Criteria**:  
✅ All 18 validation checks pass  
✅ Events significant and well-documented from primary sources  
✅ Analyses include detailed timelines, multiple RCA methods, quantified impacts, heavy citations  
✅ Multi-perspective with ≥3 viewpoints for ≥60% of analyses  
✅ Lessons actionable, transferable, non-obvious  
✅ References authoritative, diverse, contemporary to events  
✅ All links accessible or archived  
✅ No broken cross-references
