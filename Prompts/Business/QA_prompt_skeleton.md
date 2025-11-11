# Target LLM-Friendly Prompt Skeleton for Business QA

## 1. Title and Summary
- Clear, descriptive title with tag
- One-sentence purpose statement
- Brief description of capabilities

## 2. Purpose and Scope, Audience
- Primary purpose: generating interview question banks
- Scope: business-to-architecture translation
- Target audience: senior/architect/expert technical leaders
- Use case context: interview preparation

## 3. When to Use and When Not to Use
- When to use: evaluating business-technical translation skills
- When not to use: pure technical assessments, simple factual recall
- Limitations: requires business context knowledge

## 4. Inputs and Variables
- question_type: [strategic_modeling, value_risk_analysis, documentation_visualization, organizational_dynamics, architectural_translation, evolution_adaptation]
- business_context: Industry, business model, constraints
- data_sources: Reference materials available
- constraints: Time limits, word count, format requirements
- audience_level: [senior, architect, expert]
- output_format: [text, json, structured]
- confidence_policy: [high, medium, low] threshold
- ask_policy: [always_sufficient, ask_when_needed, proceed_with_assumptions]

## 5. Output Requirements and Format
- Text structure: Questions with answers, 150-300 words each
- JSON schema: 
```json
{
  "questions": [
    {
      "id": "string",
      "question": "string",
      "difficulty": ["foundational", "intermediate", "advanced"],
      "type": "string",
      "key_insight": "string",
      "answer": "string",
      "supporting_artifacts": {
        "diagram": "string",
        "table": "string",
        "formula": "string"
      },
      "sources": ["string"],
      "confidence": ["low", "medium", "high"]
    }
  ],
  "validation_report": {
    "total_questions": "number",
    "difficulty_distribution": "object",
    "coverage_metrics": "object"
  }
}
```

## 6. Constraints and Rules
- Must maintain 20/40/40 difficulty split (foundational/intermediate/advanced)
- Must include at least one diagram, table, and formula per topic cluster
- Must cite sources using [Ref: ID] format
- Must keep answers between 150-300 words
- Must avoid jargon without definition

## 7. Process for the Assistant
1. Analyze inputs and business context
2. Identify business requirements and constraints
3. Map business requirements to technical considerations
4. Generate questions that test translation ability
5. Create answers with evidence and reasoning
6. Include visual artifacts per requirements
7. Validate against constraints and rules
8. Format according to output requirements

## 8. Reasoning and Uncertainty Policy
- When factual: State with confidence and cite sources
- When interpretive: State reasoning and mention assumptions
- when uncertain: Explicitly flag the uncertainty
- When conflicting information: Acknowledge and cite multiple sources

## 9. Style and Tone Guidelines
- Business-friendly professional language
- Concise and precise terminology
- Consistent use of canonical terms
- No more than 120 characters per line
- Active voice preferred

## 10. Safety and Compliance
- No personally identifiable information
- No hallucinated sources - cite only real references
- Flag all assumptions explicitly
- Avoid unverified claims

## 11. Tools and Data Access
- Can access provided source materials and references
- Can create diagrams using Mermaid syntax
- Can format mathematical equations
- Cannot browse the internet or access external APIs

## 12. Examples
- Provide good examples following the structure
- Include edge cases and adversarial questions
- Show proper handling of missing information

## 13. Validation and Self-Review
- Preflight checklist before final output
- Post-answer self-critique process
- Evidence log requirements
- Sample validation workflow

## 14. Fallbacks and Clarifying Questions
- Decision rules for asking questions
- Templates for clarification requests
- When to proceed with assumptions vs asking

## 15. Metadata
- Version information
- Owner/maintainer details
- Last updated timestamp
- Dependencies and prerequisite knowledge

## 16. Appendices
- Glossary with canonical term definitions
- Legacy notes (preserving original content)
- Compliance matrix
- Additional reference materials