# Project Conventions  
*Last Updated: 2025-07-25 | Status: Final | Owner: Documentation Team*  

## 1. Document Structure (MECE)  
### Introduction  
- **Purpose**: Why this document exists  
- **Scope**: What's included/excluded  
- **Audience**: Who should read this  

### Body  
- **Concepts**: Definitions, principles (H2 headers)  
- **Procedures**: Numbered steps (H3 headers)  
  ```markdown
  1. Do X  
  2. Then Y  
  ```  
- **Examples**: Concrete use cases (bulleted)  
  - Case A  
  - Case B  

### Conclusion  
- **Summary**: Key takeaways  
- **Next Steps**: Actions or references  

## 2. Content Formatting  
### Hierarchy  
- H2: Main sections  
- H3: Subsections (no skipping levels)  

### References  
- **Internal**: `[Source: filename.md, line X]`  
- **External**: `[Author, Year](URL)`  

## 3. Style Guidelines  
- **Language**:  
  - Must/Should/May per RFC 2119  
  - Define acronyms on first use (e.g., MECE)  
- **Voice**: Active preferred ("Run tests" vs "Tests should be run")  

## 4. Maintenance  
- Header metadata required:  
  ```markdown
  Last Updated: YYYY-MM-DD  
  Status: Draft/Reviewed/Final  
  Owner: [Name/Team]  
  ```  
