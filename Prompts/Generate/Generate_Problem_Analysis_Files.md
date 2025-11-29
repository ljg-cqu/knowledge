# Generate Problem Analysis Files

**Last Updated**: 2025-11-29  
**Status**: Final  
**Owner**: Documentation Team

## Task

Generate problem analysis files for each problem file in `{ProblemDir}`, following `/home/zealy/nas/github/ljg-cqu/knowledge/Prompts/Problem/Analyse.md` as the canonical nine-aspects analysis framework.

## Input Parameters

- **{ProblemDir}**: Source directory containing problem files to analyze (used in directory mode)
- **{AnalysisDir}**: Target directory for generated analysis files
- **{ProblemFile}** (optional): Specific `.md` problem file to analyze  
  - If provided, analyze only this file and skip scanning `{ProblemDir}` for other problems  
  - Can be an absolute path or a path relative to `{ProblemDir}`
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
2. **Determine target problems**:
   - If `{ProblemFile}` is provided:
     - Treat `{ProblemFile}` as the only problem to analyze
     - Do **not** scan `{ProblemDir}` for additional problem files
   - If `{ProblemFile}` is not provided:
     - **Scan problem directory**: List all `.md` files in `{ProblemDir}` to identify problems requiring analysis
     - **Check existing analyses**: List all `.md` files in `{AnalysisDir}` to avoid duplication
       - Compare filenames between `{ProblemDir}` and `{AnalysisDir}`
       - Skip problems that already have corresponding analysis files (matching filename)
3. **Review supplementary sources** (if provided):
   - Read local files/directories specified in `{SupplementarySources}`
   - Parse pasted text content
   - Fetch remote URLs
   - Extract domain knowledge, technical context, and relevant background
   - Note: Treat as exploratory leads ONLY, not authoritative information
4. **For each target problem file**:
   - Read the problem file content:
     - In directory mode: from `{ProblemDir}/{FileName}.md`
     - In single-file mode: from `{ProblemFile}`
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

5. **Quality verification**: Ensure each analysis file meets framework requirements:
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
