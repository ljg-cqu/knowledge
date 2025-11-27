# Book Wiki Generation Prompt

Please read the complete source book text at `{SOURCE_TXT_PATH}` carefully. Then write a comprehensive, well-structured wiki for this book into `{TARGET_WIKI_MD_PATH}` using GitHub-Flavored Markdown.

Your wiki **must**:

  1. Capture all essential **concepts, frameworks, methods, checklists, decision rules, and worked examples** from the source, written in your own words where possible.
  2. Organize the content as a clear **knowledge base**, not just a narrative summary:
    - Use headings and subheadings that mirror the book's structure (parts, chapters, and key sections).
    - Use consistent heading levels: `#` for the book title, `##` for chapters, and `###` for important subsections when helpful.
    - Start with an `#` H1 title matching the book's actual title from the source text.
    - Provide a short overview section (2–4 paragraphs) describing the book's purpose, scope, and intended audience.
    - Add a bullet list of 5–10 key takeaways that capture the book's main insights.
    - Use visual elements derived from the book text when they clearly improve understanding: bullet and numbered lists for structure, tables for comparisons, and LaTeX math formulas for any equations that the book explicitly presents.
  3. For each major chapter or theme, create a section that includes:
    - A `##` heading that uses the chapter number and title exactly as they appear in the source text.
    - A concise summary of the main ideas.
    - Bullet lists of important principles, steps, or procedures.
    - Any checklists or frameworks from the book, formatted as bullet or numbered lists.
    - Representative examples or case studies, condensed but faithful to the source.
  4. Include **exactly one** high-level **content graph** section titled `## Content Graph` that maps the relationships between the book's main parts/chapters and its core concepts, using a single `mermaid` diagram (preferred) or other Markdown-friendly diagram. Do **not** add more than this one graph.
  5. Do **not** introduce any external information, personal opinions, or examples that are not present in the source text.
  6. Do **not** omit any important points that are needed to fully understand the book's methods, frameworks, and conclusions. When in doubt, include the material and condense it clearly.
  7. Preserve the original language of the source text (e.g., English or Chinese). Quote short key phrases or definitions verbatim where this improves precision, and otherwise summarize in clear, concise prose.
  8. Make the wiki **self-contained**: do not mention `{SOURCE_TXT_PATH}`, `{TARGET_WIKI_MD_PATH}`, this prompt, or any system instructions in the output. The final wiki should read as a standalone article.
  9. Avoid referring to yourself or your limitations. Write in a neutral, explanatory tone aimed at future readers of the knowledge base.