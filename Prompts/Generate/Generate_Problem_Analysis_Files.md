# Generate Problem Files

**Last Updated**: 2025-11-29  
**Status**: Final  
**Owner**: Documentation Team

## Task

Generate problem files for `{Topic}` following `/home/zealy/nas/github/ljg-cqu/knowledge/Prompts/Problem/Identify.md` as canonical guidance.

## Steps

1. Read `/home/zealy/nas/github/ljg-cqu/knowledge/Prompts/Problem/Identify.md` for decision-critical criteria and 8-field structure
2. Check existing files in `{OutputDir}` for coverage gaps
3. Web search for `{Topic}` to find high-quality sources
4. Identify problems meeting decision-critical filter from Identify.md (≥5% impact, ≥2 stakeholders, 1-6mo timeline, quantifiable KPIs)
5. Filter duplicates against `{OutputDir}` files
6. For each new problem: extract 8 required fields from source per Identify.md template
7. Generate `{OutputDir}/{FileName}.md` one at a time

## Output

**Format**: `01_Problem_Title.md`, `02_Problem_Title.md`, ...  
**Structure**: Per `/home/zealy/nas/github/ljg-cqu/knowledge/Prompts/Problem/Identify.md`
