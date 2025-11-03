# Shared Reference Sections

Common reference sections used across all interview prompt templates.

## Minimum Entry Requirements

| Reference section | Floor count | Notes |
| --- | --- | --- |
| Glossary, Terminology & Acronyms | ≥10 entries | Cover core concepts, domain-specific jargon, and localized terminology. |
| Codebase & Library References | ≥5 entries | Represent the primary stack components, SDKs, and supporting tooling. |
| Authoritative Literature & Reports | ≥6 entries | Blend standards, peer-reviewed work, and regulatory or industry analyses. |
| APA Style Source Citations | ≥12 total | Maintain the language mix (~60% EN / ~30% ZH / ~10% other); document gaps when unmet. |

> **Exception handling:** If a section cannot meet the floor count, explicitly state the shortfall, provide rationale, and outline a plan to source additional materials.

---

## Glossary, Terminology & Acronyms

Define key terms, acronyms, and technical vocabulary used throughout the question bank. Include language tags where applicable (e.g., `[EN]`, `[ZH]`, `[JP]`).

**Format:**
- **Term/Acronym**: Definition [Language Tag]
- **Example**: MECE (Mutually Exclusive, Collectively Exhaustive): A framework ensuring categories don't overlap and cover all possibilities [EN]

---

## Codebase & Library References

Aggregate repositories, SDKs, audits, or tooling suites cited across the question bank. Include:
- **Stack/Modules**: Technology stack and component breakdown
- **Maturity**: Development stage, version stability
- **Licensing**: Open-source licenses, commercial terms
- **Integration Hooks**: API endpoints, SDK methods, plugin architecture
- **Performance/Security Benchmarks**: Throughput, latency, vulnerability assessments
- **Distributed Consistency Guarantees**: CAP theorem positioning, consensus mechanisms
- **Reliability/HA Posture**: High availability features, failover mechanisms
- **Language Support**: Programming languages, framework compatibility

**Format:**
- **[Project/Library Name]** (GitHub: `owner/repo` | License: [Type])
  - Description: [Brief overview]
  - Stack: [Technologies]
  - Maturity: [Production/Beta/Experimental]
  - Performance: [Key metrics]
  - Security: [Audit status, vulnerability notes]

---

## Authoritative Literature & Reports

Summarize standards, white papers, yellow papers, peer-reviewed literature, regulatory reports, and other vetted references. Include:
- **Core Findings**: Key insights and conclusions
- **Credibility**: Publication venue, author credentials, peer review status
- **Language/Jurisdiction**: Source language and applicable legal/regulatory context

**Format:**
- **[Title]** (Year) [Language Tag]
  - Authors: [Names/Organization]
  - Type: [Standard/White Paper/Academic Paper/Regulatory Report]
  - Key Findings: [Summary]
  - Credibility: [Peer-reviewed/Industry standard/Regulatory authority]
  - Jurisdiction: [Applicable regions/markets]

---

## APA Style Source Citations

- **References**: List all sources cited in the answers, grouped by source language with the targeted distribution (~60% English, ~30% Chinese, ~10% other languages). If credible non-English sources are not available, document the gap and default to high-quality English sources.

- **Format**: Follow APA 7th edition (author, year, title, source, DOI/URL when available) and include language tags (e.g., `[EN]`, `[ZH]`, `[JP]`).

- **Verification**: Ensure each reference is credible, jurisdiction-appropriate, and directly supports the content; highlight regulatory or legal sources when applicable.

**Example:**
```
Smith, J., & Wang, L. (2024). Blockchain consensus mechanisms: A comparative analysis. 
    Journal of Distributed Systems, 15(3), 245-267. https://doi.org/10.xxxx/jds.2024.15.3.245 [EN]

张伟, & 李娜. (2024). 区块链技术在供应链金融中的应用研究. 
    计算机科学, 51(2), 88-95. [ZH]

Nakamoto, S. (2008). Bitcoin: A peer-to-peer electronic cash system. 
    https://bitcoin.org/bitcoin.pdf [EN]
```

---

## Usage Notes

When using these sections in your prompt templates:

1. **Reference this file** from your template:
   ```markdown
   See [Shared Reference Sections](../Shared_References.md) for reference formatting.
   ```

2. **Populate sections** with actual content specific to your domain/topic

3. **Maintain consistency** in formatting across all references

4. **Update centrally** - changes here apply to all templates using this file
