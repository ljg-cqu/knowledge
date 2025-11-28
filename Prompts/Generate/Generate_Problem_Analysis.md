# Orchestrator: Nine-Aspects Analysis for Problems

**Prompt**: `/home/zealy/nas/github/ljg-cqu/knowledge/Prompts/Problem/Analysis/Nine_Aspects_Analysis.md`  
**Problems**: `<PATH_TO_PROBLEM_FILE/{FileName}.md>`  
**Output**: `<PATH_TO_OUTPUT_FILE/{FileName}.md>`  
**{FileName}**: `<BASENAME_WITHOUT_EXTENSION>`

For each `Q: ... A: ...` in Problems:
- Call LLM with full prompt + single Q/A as 【Input】(self-contained)
- Append to Output as `## Problem N – <short title>` (preserve order)

Handle problems one by one to avoid context limits.