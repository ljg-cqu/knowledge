# Generate Problem Files

**Last Updated**: 2025-11-29  
**Status**: Final  
**Owner**: Documentation Team

## Task

Generate problem files for `{Topic}` following `/home/zealy/nas/github/ljg-cqu/knowledge/Prompts/Problem/Identify.md` as canonical guidance.

## Input Parameters

- **{Topic}**: The subject area for problem generation
- **{OutputDir}**: Target directory for generated problem files
- **{SupplementarySources}** (optional): Additional reference materials including:
  - Local file paths or directory paths
  - Pasted text content
  - Remote URLs

### ⚠️ Warning: Supplementary Sources Quality

**CRITICAL**: Supplementary sources may contain:
- Low-quality, outdated, or incomplete information
- Inaccurate, misleading, or factually incorrect content
- Biased perspectives or unverified claims

**Usage Guidelines**:
- Treat supplementary sources ONLY as reference material, inspiration, or initial cues
- NEVER directly copy or trust information from supplementary sources without verification
- ALWAYS cross-validate all facts, data, and claims against authoritative web sources
- Use web search to find current, high-quality, peer-reviewed, or industry-standard sources
- Prioritize accuracy and precision over expediency

## Steps

1. Read `/home/zealy/nas/github/ljg-cqu/knowledge/Prompts/Problem/Identify.md` for decision-critical criteria and 8-field structure
2. Check existing files in `{OutputDir}` for coverage gaps
3. **Review supplementary sources** (if provided):
   - Read local files/directories specified in `{SupplementarySources}`
   - Parse pasted text content
   - Fetch remote URLs
   - Extract potential problem themes, keywords, and areas of interest
   - Note: Treat as exploratory leads ONLY, not authoritative information
4. **Web search for `{Topic}`** using high-quality, authoritative sources:
   - Academic papers, industry reports, official documentation
   - Reputable news outlets, expert blogs, conference proceedings
   - Verify and cross-reference any insights from supplementary sources
   - Ensure all factual claims are supported by multiple reliable sources
5. Identify problems meeting decision-critical filter from Identify.md (≥5% impact, ≥2 stakeholders, 1-6mo timeline, quantifiable KPIs)
6. Filter duplicates against `{OutputDir}` files
7. For each new problem: extract 8 required fields from verified, authoritative sources per Identify.md template
8. Generate `{OutputDir}/{FileName}.md` one at a time

## Output

**Format**: `01_Problem_Title.md`, `02_Problem_Title.md`, ...  
**Structure**: Per `/home/zealy/nas/github/ljg-cqu/knowledge/Prompts/Problem/Identify.md`
