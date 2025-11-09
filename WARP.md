# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a Markdown-only knowledge base repository organized as topic-first folders. No compiled code, tests, or runtime components exist in this repository.

## Common Commands

### Linting (optional)
```bash
npx markdownlint-cli2 "**/*.md"
```

### Formatting (optional)
```bash
npx prettier -w "**/*.md"
```

### Link checking (optional)
```bash
npx markdown-link-check "**/*.md"
```

### Spell/style checking (optional)
```bash
vale "**/*.md"
```

## Repository Architecture

### Folder Structure
The repository follows a topic-first organization pattern:
- AI/ - Topics related to artificial intelligence
- Blockchain/ - Blockchain technology and concepts
- ComputerScience/ - Computer science fundamentals
- languages/ - Programming languages and linguistics
- Thinking/ - Cognitive processes and thinking frameworks
- Workplace/ - Professional and work-related topics
- 'RDR (Reflect, Do, Rest)/' - Productivity methodology
- And more specialized topic folders

### File Naming Conventions
- Files use bracketed tags to convey note type:
  - `[scan]` - Overview documents
  - `[crit]` - Critiques
  - `[lang]` - Language notes
  - `[deve]` - Development topics
  - `[prac]` - Practice materials
  - `[queX]` - Question-based content (where X is the question level)
  - Numeric prefixes like `[1-q0]` for ordering
- Files are standalone notes (not part of a multi-file system)
- Words in filenames are typically separated by spaces

### Authoring Conventions
- GitHub-Flavored Markdown with clear H1 headers matching the title
- Concise sections with bullet lists preferred
- Fenced code blocks with language tags (e.g., ```bash, ```go)
- Relative links to other notes with descriptive link text
- Simple GitHub Markdown tables when helpful
- Mermaid diagrams allowed in fenced ```mermaid blocks
- Lines kept under 120 characters for diff readability
- No trailing whitespace

### Content Organization Principles
- Place new notes under the most specific existing folder
- Reuse existing bracketed tag conventions for consistency
- Each note is self-contained and internally consistent

## Development Guidelines

### Version Control
- Make small, topic-scoped commits with informative messages
- Group edits by note/topic rather than sweeping changes
- Follow conventional commit format when possible

### Safety Rules
- Never add secrets or sensitive information
- External command examples should not leak tokens/keys
- Avoid including any personal or confidential information