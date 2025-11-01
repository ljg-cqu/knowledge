# Exam Prompt Templates

This folder contains separate prompt templates for different exam item types that are not covered by the Q&A-only prompts in `Prompts_(Deep).md`.

Each file is self-contained and includes:
- Purpose and when to use the prompt
- A ready-to-use prompt template (editable)
- A short example
- Grading/rubric notes and machine-grading tips where applicable

Files kept in this folder:
- `MCQ.md` — multiple-choice
- `Cloze.md` — fill-in-the-blank / cloze
- `ShortAnswer_Calc.md` — short answer / numeric calculation
- `CaseStudy.md` — scenario-based multi-part
- `Coding_Task.md` — coding prompt (machine-gradable)
- `Debugging_Task.md` — debugging prompt
 - `Data_Interpretation.md` — data/graph/table questions
 - `TrueFalse.md` — true/false statements (binary items)

Note: other prompt files (essays, image-based, adaptive UI, oral viva, peer assessment, practical labs, project portfolios, audio/video, accessibility, integrity/proctoring, multimodal simulation) were removed to keep the folder minimal per project preference. If you want any of them restored, I can revert the deletions or recreate simplified versions.

How to use
1. Open the template file matching your item type.
2. Edit the bracketed fields ([...]) to supply the stem, options, assets, or starter code.
3. Use the grading notes to build rubrics or machine checks (unit tests, answer keys).

If you want, I can also:
- Insert links back to specific prompts in `Prompts_(Deep).md`.
- Generate a sample MCQ bank or a runnable coding test harness for one coding prompt.
 - Help set up an `assets/` subfolder (already present) to store images, datasets, starter code, and transcripts. Put image files and matching alt-text files in `assets/` and reference them by relative path from the individual prompt files.
