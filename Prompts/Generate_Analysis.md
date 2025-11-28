# Orchestrator: Nine-Aspects Analysis for Problems
 
Prompt: `/home/zealy/nas/github/ljg-cqu/knowledge/Prompts/Analysis/Nine_Aspects_Analysis.md`
Problems: `<PATH_TO_PROBLEM_FILE/{FileName}.md>`
Output: `<PATH_TO_OUTPUT_FILE/{FileName}.md>`
{FileName} = `<BASENAME_WITHOUT_EXTENSION>`

For each `Q: ... A: ...` in Problems:
- Call the LLM with the full "LLM Prompt Template: Nine-Aspects Problem Analysis" plus that single Q/A as the filled 【Input】. The prompt must be fully self-contained.
- Append the answer to Output as `## Problem N – <short title>` in the same order as in Problems.