# Generate Problem Analysis Files

**Last Updated**: 2025-11-29  
**Status**: Final  
**Owner**: Documentation Team

## Task

Generate problem analysis files for each problem file in `{ProblemDir}`, following `/home/zealy/nas/github/ljg-cqu/knowledge/Prompts/Problem/Analyse.md` as the canonical nine-aspects analysis framework.

## Input Parameters

- **{ProblemDir}**: Source directory containing problem files to analyze
- **{AnalysisDir}**: Target directory for generated analysis files
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

1. **Read the analysis framework**: Load `/home/zealy/nas/github/ljg-cqu/knowledge/Prompts/Problem/Analyse.md` to understand the nine-aspects analysis structure, guidelines, and output requirements
2. **Scan problem directory**: List all `.md` files in `{ProblemDir}` to identify problems requiring analysis
3. **Check existing analyses**: List all `.md` files in `{AnalysisDir}` to avoid duplication
   - Compare filenames between `{ProblemDir}` and `{AnalysisDir}`
   - Skip problems that already have corresponding analysis files (matching filename)
4. **Review supplementary sources** (if provided):
   - Read local files/directories specified in `{SupplementarySources}`
   - Parse pasted text content
   - Fetch remote URLs
   - Extract domain knowledge, technical context, and relevant background
   - Note: Treat as exploratory leads ONLY, not authoritative information
5. **For each unanalyzed problem file**:
   - Read the problem file content from `{ProblemDir}/{FileName}.md`
   - Extract problem statement, context, constraints, stakeholders, and goals
   - Conduct web search for authoritative sources related to the problem domain:
     - Academic papers, industry reports, official documentation
     - Technical benchmarks, case studies, expert analyses
     - Verify and cross-reference any insights from supplementary sources
   - Apply the nine-aspects framework from Analyse.md:
     - Fill all 【Input】 fields with problem-specific data
     - Generate analysis following the full output structure (sections 1-12)
     - Include mandatory in-line citations (≥70% coverage, ≥3 per section)
     - Add Glossary (section 11) and References (section 12)
   - Generate `{AnalysisDir}/{FileName}.md` with **identical filename** as source problem file

6. **Quality verification**: Ensure each analysis file meets framework requirements:
   - All nine aspects + context recap covered
   - ≥70% citation coverage with source quality tiers
   - Glossary with ≥10 entries
   - References section with ≥8-12 sources
   - Actionable recommendations with metrics and timelines

## Output

**Format**: `{AnalysisDir}/{FileName}.md` (exact match to `{ProblemDir}/{FileName}.md`)  
**Structure**: Per `/home/zealy/nas/github/ljg-cqu/knowledge/Prompts/Problem/Analyse.md` nine-aspects framework  
**Correspondence**: 1:1 mapping between problem files and analysis files by filename

### Example

**Input**:
- `{ProblemDir}/01_API_Latency_Issue.md`
- `{ProblemDir}/02_Cache_Optimization.md`

**Output**:
- `{AnalysisDir}/01_API_Latency_Issue.md` (nine-aspects analysis)
- `{AnalysisDir}/02_Cache_Optimization.md` (nine-aspects analysis)
