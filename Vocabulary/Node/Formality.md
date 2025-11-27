# Node Vocabulary: Formality Variants

1. **Original Expression**: This callback is messed up (context: pointing out problematic nested callbacks)
   **Context**: Code review comment on deeply nested callback structure
   
   **Core Intent**: Indicate that the callback structure is problematic and needs refactoring
   
   **Casual**: This callback is messed up—let's refactor it.  
   *Characteristics*: slang "messed up", direct, informal vocabulary  
   *Use when*: close teammates, informal chat, internal discussions
   
   **Semi-Formal**: This callback structure needs refactoring.  
   *Characteristics*: neutral vocabulary, direct statement, professional tone  
   *Use when*: code reviews, team meetings, standard professional communication
   
   **Formal**: The current callback implementation exhibits excessive nesting and requires refactoring.  
   *Characteristics*: technical vocabulary, complete sentences, precise description  
   *Use when*: documentation, formal reviews, external communication
   
   **Humorous**: We've got a textbook case of callback hell here! 🙈  
   *Characteristics*: idiom "callback hell", emoji, playful tone  
   *Use when*: friendly team culture, building rapport, light moments  
   *Avoid when*: serious bugs, external communication, formal contexts
   
   **Lively**: Whoa, these callbacks are nested like crazy!  
   *Characteristics*: exclamation, emphatic language, energetic tone  
   *Use when*: expressing surprise, team discussions, informal settings
   
   **Empathetic**: I know callbacks can get tricky—maybe we could simplify this structure?  
   *Characteristics*: acknowledgment of difficulty, suggestion rather than criticism  
   *Use when*: junior developers' code, learning situations, supportive feedback
   
   **Register Selection Guide**:
   - *Power Distance*: casual with peers, formal with management or external
   - *Social Distance*: casual with close team, formal with new members or external
   - *Gravity of Situation*: casual for minor issues, formal for critical bugs
   - *Cultural Context*: tech culture tends informal, but adjust for formal organizations
   - *Medium*: chat allows casual, documentation requires formal
   
   **Common Mistakes**:
   - Using slang like "messed up" in documentation
   - Being too formal in team chat ("exhibits excessive nesting")
   - Using humor in serious production bugs
   
   **Cultural Notes**: Tech culture generally informal, but startups more casual than enterprise. Adjust formality based on company culture.
   
   **Context Examples**:
   - **Situation 1**: Slack message to teammate → **Appropriate Variant**: Casual or Humorous
   - **Situation 2**: Pull request comment → **Appropriate Variant**: Semi-Formal
   - **Situation 3**: Technical documentation → **Appropriate Variant**: Formal

1. **Original Expression**: You need to add error handling here (context: code review feedback)
   **Context**: Reviewing pull request that lacks error handling
   
   **Core Intent**: Request that error handling be added to the code
   
   **Casual**: You should add error handling here.  
   *Characteristics*: "should" softens "need", direct, simple  
   *Use when*: peer code reviews, friendly team environment
   
   **Semi-Formal**: Error handling should be added to this function.  
   *Characteristics*: passive voice, focus on action not person, professional  
   *Use when*: formal code reviews, standard PR comments, team communication
   
   **Formal**: It is recommended that error handling be implemented for this operation.  
   *Characteristics*: passive construction, formal vocabulary, impersonal  
   *Use when*: formal documentation, external reviews, architectural documents
   
   **Humorous**: Let's catch those errors before they catch us! 😄  
   *Characteristics*: playful metaphor, emoji, light tone  
   *Use when*: friendly code reviews, building team rapport  
   *Avoid when*: security issues, critical bugs, external communication
   
   **Lively**: This definitely needs error handling!  
   *Characteristics*: emphasis with "definitely", exclamation  
   *Use when*: emphasizing importance, team discussions
   
   **Empathetic**: I notice there's no error handling yet—would you like help adding it?  
   *Characteristics*: observation not criticism, offers help, collaborative  
   *Use when*: junior developers, learning situations, mentoring
   
   **Register Selection Guide**:
   - *Power Distance*: casual with peers, formal upward, semi-formal downward with respect
   - *Social Distance*: casual within team, formal with external reviewers
   - *Gravity of Situation*: more formal for critical security/reliability issues
   - *Cultural Context*: adjust to team's feedback culture
   - *Medium*: inline comments allow casual, summary requires more formal
   
   **Common Mistakes**:
   - Too direct: "You forgot error handling" (accusatory)
   - Too vague: "Maybe consider errors?" (unclear requirement)
   - Wrong tone: Using humor for critical security issues
   
   **Cultural Notes**: Code review culture varies widely. Some teams prefer very direct feedback, others more diplomatic.
   
   **Context Examples**:
   - **Situation 1**: Informal PR comment to peer → **Appropriate Variant**: Casual
   - **Situation 2**: Formal architecture review → **Appropriate Variant**: Formal
   - **Situation 3**: Mentoring junior developer → **Appropriate Variant**: Empathetic

1. **Original Expression**: The API is slow (context: performance issue)
   **Context**: Discussing API performance problems
   
   **Core Intent**: Communicate that the API has performance issues
   
   **Casual**: The API is slow.  
   *Characteristics*: simple adjective, direct, informal  
   *Use when*: quick communication, team chat, familiar colleagues
   
   **Semi-Formal**: The API has performance issues.  
   *Characteristics*: technical vocabulary, neutral tone, professional  
   *Use when*: status reports, team meetings, issue descriptions
   
   **Formal**: The API exhibits suboptimal response latency.  
   *Characteristics*: precise technical terminology, formal vocabulary  
   *Use when*: technical documentation, client communication, formal reports
   
   **Humorous**: This API is slower than a turtle on vacation! 🐢  
   *Characteristics*: simile, exaggeration, emoji, playful  
   *Use when*: friendly team discussions, expressing frustration lightly  
   *Avoid when*: client meetings, formal reports, blame situations
   
   **Lively**: Wow, this API is really dragging!  
   *Characteristics*: interjection "wow", colloquial "dragging", emphasis  
   *Use when*: expressing frustration, team discussions, informal settings
   
   **Empathetic**: I know optimizing APIs can be challenging—the response time seems a bit high.  
   *Characteristics*: acknowledges difficulty, softened observation, supportive  
   *Use when*: providing feedback to developers, collaborative problem-solving
   
   **Register Selection Guide**:
   - *Power Distance*: casual with team, formal with management/clients
   - *Social Distance*: casual internally, formal externally
   - *Gravity of Situation*: formal for critical production issues, casual for minor
   - *Cultural Context*: adjust for blame culture vs. learning culture
   - *Medium*: chat allows casual, status report requires formal
   
   **Common Mistakes**:
   - Too vague: "It's not great" (unclear what's wrong)
   - Too blaming: "You made it slow" (accusatory)
   - Wrong priority: Joking about critical production issue
   
   **Cultural Notes**: Performance discussions can be sensitive. Frame as technical issue, not developer failure.
   
   **Context Examples**:
   - **Situation 1**: Slack to team → **Appropriate Variant**: Casual or Lively
   - **Situation 2**: Sprint retrospective → **Appropriate Variant**: Semi-Formal
   - **Situation 3**: Client status report → **Appropriate Variant**: Formal

1. **Original Expression**: Use async/await instead of callbacks (context: suggesting code improvement)
   **Context**: Recommending modern async pattern
   
   **Core Intent**: Suggest replacing callbacks with async/await syntax
   
   **Casual**: Use async/await instead of callbacks.  
   *Characteristics*: imperative form, direct, simple  
   *Use when*: peer suggestions, team discussions, quick feedback
   
   **Semi-Formal**: Consider using async/await instead of callbacks.  
   *Characteristics*: "consider" softens directive, professional suggestion  
   *Use when*: code reviews, formal suggestions, team recommendations
   
   **Formal**: It is recommended to employ async/await syntax rather than callback-based patterns.  
   *Characteristics*: passive construction, formal vocabulary, technical precision  
   *Use when*: coding standards documentation, formal guidelines, architecture docs
   
   **Humorous**: Let's escape callback hell and embrace the async/await paradise! 🌴  
   *Characteristics*: metaphor "paradise vs. hell", emoji, enthusiastic  
   *Use when*: advocating modern practices, team discussions, selling ideas  
   *Avoid when*: resistance to change, formal documentation, external communication
   
   **Lively**: Async/await is way cleaner—definitely worth switching!  
   *Characteristics*: emphatic "way cleaner", "definitely", enthusiastic  
   *Use when*: advocating improvements, building excitement for change
   
   **Empathetic**: I know callbacks are familiar, but async/await might make this easier to maintain.  
   *Characteristics*: acknowledges current approach, focuses on benefits, gentle  
   *Use when*: suggesting changes to established code, senior developers set in ways
   
   **Register Selection Guide**:
   - *Power Distance*: suggestion form with seniors, direct with peers
   - *Social Distance*: casual with team, formal in written guidelines
   - *Gravity of Situation*: casual for nice-to-have, formal for critical improvements
   - *Cultural Context*: some teams prefer direct, others diplomatic
   - *Medium*: chat allows direct, documentation needs formal
   
   **Common Mistakes**:
   - Too pushy: "You must use async/await" (overbearing)
   - Too weak: "Maybe think about async?" (unclear recommendation)
   - Missing context: Not explaining why async/await is better
   
   **Cultural Notes**: Balance between progressive improvement and respecting existing code. Some developers resist "fads."
   
   **Context Examples**:
   - **Situation 1**: PR comment to peer → **Appropriate Variant**: Casual or Semi-Formal
   - **Situation 2**: Refactoring proposal → **Appropriate Variant**: Lively
   - **Situation 3**: Coding standards doc → **Appropriate Variant**: Formal

1. **Original Expression**: This won't work in production (context: identifying deployment issue)
   **Context**: Reviewing code that will fail in production environment
   
   **Core Intent**: Warn that code will fail in production and needs fixing
   
   **Casual**: This won't work in production.  
   *Characteristics*: contraction "won't", direct, simple  
   *Use when*: team discussions, quick alerts, peer communication
   
   **Semi-Formal**: This approach will not function correctly in production.  
   *Characteristics*: no contraction, "function correctly" more precise, professional  
   *Use when*: code reviews, issue reports, team communication
   
   **Formal**: This implementation is incompatible with production environment requirements.  
   *Characteristics*: formal vocabulary, precise technical language, impersonal  
   *Use when*: formal reports, documentation, external communication
   
   **Humorous**: Houston, we have a problem—this won't survive production! 🚀  
   *Characteristics*: pop culture reference, dramatic, playful  
   *Use when*: catching issues early, friendly team culture  
   *Avoid when*: actual production incidents, blame situations, external
   
   **Lively**: Red flag—this will break in production!  
   *Characteristics*: metaphor "red flag", emphatic, urgent tone  
   *Use when*: raising urgent concerns, getting attention
   
   **Empathetic**: I'm concerned this might cause issues in production—have you tested with production config?  
   *Characteristics*: "concerned" not accusing, question invites discussion, supportive  
   *Use when*: potentially overlooked issues, collaborative problem-solving
   
   **Register Selection Guide**:
   - *Power Distance*: direct with peers, respectful with seniors, clear with juniors
   - *Social Distance*: casual within team, formal with external stakeholders
   - *Gravity of Situation*: more formal for critical issues, casual for caught early
   - *Cultural Context*: some cultures prefer directness, others diplomacy
   - *Medium*: urgent chat allows casual, written report requires formal
   
   **Common Mistakes**:
   - Too alarmist: "This will destroy everything!" (exaggeration)
   - Too soft: "Might not be ideal..." (understating critical issue)
   - Blaming: "You broke production" (accusatory)
   
   **Cultural Notes**: Production issues are serious. Balance urgency with professionalism. Avoid blame, focus on solutions.
   
   **Context Examples**:
   - **Situation 1**: Pre-deployment code review → **Appropriate Variant**: Casual or Semi-Formal
   - **Situation 2**: Blocking PR approval → **Appropriate Variant**: Semi-Formal
   - **Situation 3**: Incident report → **Appropriate Variant**: Formal

1. **Original Expression**: I don't understand this code (context: requesting clarification)
   **Context**: Encountering unclear or complex code in review
   
   **Core Intent**: Request clarification or explanation of code
   
   **Casual**: I don't get what this code does.  
   *Characteristics*: "don't get" informal, direct, simple  
   *Use when*: peer discussions, team chat, comfortable relationships
   
   **Semi-Formal**: Could you explain what this code is doing?  
   *Characteristics*: polite question, "could you" softens request, professional  
   *Use when*: code reviews, formal requests, standard team communication
   
   **Formal**: I would appreciate clarification regarding the intent of this implementation.  
   *Characteristics*: formal request form, precise vocabulary, very polite  
   *Use when*: formal reviews, external code review, senior-to-senior
   
   **Humorous**: This code speaks a language I don't know yet! Mind translating? 😅  
   *Characteristics*: playful metaphor, emoji, self-deprecating  
   *Use when*: friendly requests, building rapport, admitting confusion lightly  
   *Avoid when*: code is actually bad (comes across as passive-aggressive)
   
   **Lively**: Whoa, what's happening here? Walk me through it!  
   *Characteristics*: interjection, energetic request, enthusiastic  
   *Use when*: collaborative learning, friendly environment
   
   **Empathetic**: This section is a bit complex for me—would you mind explaining your approach?  
   *Characteristics*: admits own limitation, polite request, respectful  
   *Use when*: any situation, safe default, shows humility
   
   **Register Selection Guide**:
   - *Power Distance*: empathetic with seniors, casual with peers, clear with juniors
   - *Social Distance*: casual with close team, formal with external or new members
   - *Gravity of Situation*: casual for learning, formal for critical review
   - *Cultural Context*: some cultures see admitting confusion as weakness—adjust
   - *Medium*: chat allows casual, formal review needs professional
   
   **Common Mistakes**:
   - Too aggressive: "This code makes no sense" (insulting)
   - Too apologetic: "Sorry, I'm probably being stupid but..." (undermines self)
   - Passive-aggressive: Using humor to mask criticism
   
   **Cultural Notes**: Admitting confusion is professional, not weak. Good code reviews involve questions.
   
   **Context Examples**:
   - **Situation 1**: PR comment to peer → **Appropriate Variant**: Casual or Empathetic
   - **Situation 2**: Architectural review → **Appropriate Variant**: Semi-Formal
   - **Situation 3**: External consultant review → **Appropriate Variant**: Formal

1. **Original Expression**: Great job on this feature! (context: praising completed work)
   **Context**: Recognizing successful feature implementation
   
   **Core Intent**: Express appreciation and praise for quality work
   
   **Casual**: Great job on this!  
   *Characteristics*: brief, enthusiastic, direct praise  
   *Use when*: quick recognition, team chat, peer-to-peer
   
   **Semi-Formal**: Excellent work on this feature implementation.  
   *Characteristics*: "excellent" professional, specific about what, neutral tone  
   *Use when*: formal recognition, PR approvals, team meetings
   
   **Formal**: The implementation of this feature demonstrates exemplary technical proficiency.  
   *Characteristics*: formal vocabulary, detailed description, professional  
   *Use when*: performance reviews, formal recognition, external communication
   
   **Humorous**: This feature is absolutely fire! 🔥  
   *Characteristics*: slang "fire", emoji, very enthusiastic  
   *Use when*: celebrating wins, building morale, friendly team  
   *Avoid when*: formal contexts, may seem insincere if overused
   
   **Lively**: Wow, this feature is amazing! Really impressive work!  
   *Characteristics*: interjection, multiple exclamations, enthusiastic  
   *Use when*: genuine excitement, celebrating achievements, energizing team
   
   **Empathetic**: I know you worked hard on this—it shows! The feature is excellent.  
   *Characteristics*: acknowledges effort, connects work to outcome, warm  
   *Use when*: recognizing struggle, difficult features, meaningful recognition
   
   **Register Selection Guide**:
   - *Power Distance*: any level can praise, adjust formality to relationship
   - *Social Distance*: casual with close team, formal in public recognition
   - *Gravity of Situation*: match enthusiasm to achievement size
   - *Cultural Context*: some cultures prefer understated, others effusive praise
   - *Medium*: chat allows casual, email/review needs more formal
   
   **Common Mistakes**:
   - Too generic: "Good job" without specifics (seems perfunctory)
   - Too effusive: "BEST CODE EVER!" (loses credibility)
   - Unbalanced: Only praising some team members
   
   **Cultural Notes**: Recognition matters for morale. Be genuine and specific for maximum impact.
   
   **Context Examples**:
   - **Situation 1**: Slack to teammate → **Appropriate Variant**: Casual or Lively
   - **Situation 2**: PR approval comment → **Appropriate Variant**: Semi-Formal
   - **Situation 3**: Performance review → **Appropriate Variant**: Formal

1. **Original Expression**: This is broken (context: reporting a bug)
   **Context**: Identifying non-functional code or feature
   
   **Core Intent**: Report that something is not working correctly
   
   **Casual**: This is broken.  
   *Characteristics*: simple, direct, informal  
   *Use when*: quick bug reports, team chat, familiar colleagues
   
   **Semi-Formal**: This functionality is not working correctly.  
   *Characteristics*: precise description, professional vocabulary, neutral  
   *Use when*: bug reports, issue tracking, standard communication
   
   **Formal**: This component exhibits a functional defect requiring remediation.  
   *Characteristics*: formal technical vocabulary, precise classification  
   *Use when*: formal bug reports, external communication, documentation
   
   **Humorous**: Oops, looks like this decided to take a vacation! 🏖️  
   *Characteristics*: playful metaphor, emoji, lighthearted  
   *Use when*: minor bugs, friendly environment, diffusing tension  
   *Avoid when*: critical production bugs, user-facing issues, blame situations
   
   **Lively**: Uh-oh, we've got a bug here!  
   *Characteristics*: interjection, colloquial, energetic  
   *Use when*: catching bugs during development, team discussions
   
   **Empathetic**: I think there might be an issue here—it's not behaving as expected.  
   *Characteristics*: tentative "might", focuses on behavior not blame, gentle  
   *Use when*: reporting bugs in others' code, collaborative debugging
   
   **Register Selection Guide**:
   - *Power Distance*: casual with peers, professional upward, clear downward
   - *Social Distance*: casual within team, formal with external stakeholders
   - *Gravity of Situation*: formal for critical bugs, casual for minor issues
   - *Cultural Context*: some cultures prefer direct, others indirect bug reporting
   - *Medium*: urgent chat allows casual, ticket system needs clear description
   
   **Common Mistakes**:
   - Too vague: "Something's wrong" (not actionable)
   - Too blaming: "You broke this" (accusatory)
   - Wrong tone: Joking about critical production bug
   
   **Cultural Notes**: Bugs are normal, not failures. Focus on description, reproduction steps, and solutions, not blame.
   
   **Context Examples**:
   - **Situation 1**: Finding bug in own code → **Appropriate Variant**: Casual
   - **Situation 2**: Bug report ticket → **Appropriate Variant**: Semi-Formal
   - **Situation 3**: Critical production issue → **Appropriate Variant**: Formal

1. **Original Expression**: Can you check this? (context: requesting code review)
   **Context**: Asking someone to review code or implementation
   
   **Core Intent**: Request someone review or verify work
   
   **Casual**: Can you check this?  
   *Characteristics*: brief, direct, simple modal  
   *Use when*: quick peer reviews, informal requests, familiar colleagues
   
   **Semi-Formal**: Could you review this when you have a chance?  
   *Characteristics*: "could" more polite than "can", acknowledges their time  
   *Use when*: formal review requests, respectful communication, standard PRs
   
   **Formal**: I would appreciate your review and feedback on this implementation.  
   *Characteristics*: formal request form, specific about need, very polite  
   *Use when*: formal reviews, senior reviewers, external code review
   
   **Humorous**: Mind taking a peek at this? Fresh code hot off the press! 👀  
   *Characteristics*: playful language "peek", metaphor, emoji  
   *Use when*: friendly team culture, regular reviews, building rapport  
   *Avoid when*: urgent critical reviews, unfamiliar reviewers
   
   **Lively**: Hey, would love your eyes on this!  
   *Characteristics*: enthusiastic, casual greeting, values their input  
   *Use when*: peer reviews, collaborative environment
   
   **Empathetic**: I know you're busy, but would you mind reviewing this when you get a chance?  
   *Characteristics*: acknowledges their workload, patient request, considerate  
   *Use when*: reviewing with busy colleagues, respectful requests, any situation
   
   **Register Selection Guide**:
   - *Power Distance*: casual with peers, formal with seniors, clear with juniors
   - *Social Distance*: casual with team, formal with external reviewers
   - *Gravity of Situation*: match urgency to formality
   - *Cultural Context*: some cultures expect direct requests, others prefer softer
   - *Medium*: chat allows casual, PR description should be clear
   
   **Common Mistakes**:
   - Too demanding: "Review this now" (disrespectful)
   - Too apologetic: "Sorry to bother but..." (excessive)
   - No context: Not explaining what needs review or why
   
   **Cultural Notes**: Respect reviewers' time. Provide context about urgency and complexity. Make it easy for them to help.
   
   **Context Examples**:
   - **Situation 1**: Slack to teammate → **Appropriate Variant**: Casual or Lively
   - **Situation 2**: PR request to senior dev → **Appropriate Variant**: Semi-Formal or Empathetic
   - **Situation 3**: External consultant review → **Appropriate Variant**: Formal

1. **Original Expression**: The documentation needs work (context: feedback on docs)
   **Context**: Providing feedback that documentation is insufficient
   
   **Core Intent**: Indicate that documentation quality or completeness is inadequate
   
   **Casual**: The docs need work.  
   *Characteristics*: abbreviation "docs", direct, simple  
   *Use when*: internal feedback, team discussions, familiar colleagues
   
   **Semi-Formal**: The documentation could be improved.  
   *Characteristics*: modal "could", positive framing (improvement), diplomatic  
   *Use when*: formal feedback, review comments, standard communication
   
   **Formal**: The documentation requires enhancement to meet professional standards.  
   *Characteristics*: formal vocabulary, specific about need, professional  
   *Use when*: formal reviews, external feedback, quality standards discussions
   
   **Humorous**: These docs need some TLC! 💝  
   *Characteristics*: abbreviation "TLC" (tender loving care), emoji, lighthearted  
   *Use when*: friendly feedback, internal discussions, motivating improvement  
   *Avoid when*: critical missing docs, external projects, formal contexts
   
   **Lively**: Let's beef up these docs—they're a bit thin!  
   *Characteristics*: colloquial "beef up", metaphor "thin", energetic  
   *Use when*: motivating documentation work, team discussions
   
   **Empathetic**: I know docs often get left till last, but users might need more detail here.  
   *Characteristics*: acknowledges reality, focuses on user needs, constructive  
   *Use when*: encouraging documentation, supporting developers, collaborative
   
   **Register Selection Guide**:
   - *Power Distance*: diplomatic regardless of hierarchy
   - *Social Distance*: casual internally, formal for external/open-source
   - *Gravity of Situation*: formal if docs are critical (API, security)
   - *Cultural Context*: some developers sensitive about docs criticism
   - *Medium*: chat allows casual, PR feedback should be constructive
   
   **Common Mistakes**:
   - Too harsh: "The docs are terrible" (demotivating)
   - Too vague: "More docs would be good" (not actionable)
   - Not offering help: Criticizing without supporting
   
   **Cultural Notes**: Documentation often neglected. Frame feedback positively. Offer specific suggestions or help.
   
   **Context Examples**:
   - **Situation 1**: Internal code review → **Appropriate Variant**: Casual or Empathetic
   - **Situation 2**: Open-source contribution → **Appropriate Variant**: Semi-Formal
   - **Situation 3**: Documentation quality review → **Appropriate Variant**: Formal

1. **Original Expression**: Let's refactor this mess (context: proposing code cleanup)
   **Context**: Suggesting refactoring of disorganized or complex code
   
   **Core Intent**: Propose refactoring to improve code quality
   
   **Casual**: Let's refactor this.  
   *Characteristics*: direct, collaborative "let's", simple  
   *Use when*: team decisions, peer discussions, shared responsibility
   
   **Semi-Formal**: This code would benefit from refactoring.  
   *Characteristics*: neutral observation, "would benefit" diplomatic, professional  
   *Use when*: code reviews, formal suggestions, technical discussions
   
   **Formal**: I recommend refactoring this implementation to improve maintainability.  
   *Characteristics*: formal recommendation, specific benefit stated, professional  
   *Use when*: formal proposals, architecture reviews, documentation
   
   **Humorous**: Time for some spring cleaning in this code! 🧹  
   *Characteristics*: metaphor "spring cleaning", emoji, playful  
   *Use when*: motivating cleanup work, team discussions, building energy  
   *Avoid when*: someone else's recent code (seems critical), formal proposals
   
   **Lively**: Let's give this code a makeover!  
   *Characteristics*: enthusiastic metaphor "makeover", energetic  
   *Use when*: motivating refactoring, team initiatives, positive framing
   
   **Empathetic**: This code has grown complex over time—maybe we could simplify it together?  
   *Characteristics*: explains how it happened (not blame), collaborative approach  
   *Use when*: legacy code, team refactoring, respecting previous work
   
   **Register Selection Guide**:
   - *Power Distance*: collaborative with peers, proposal form with seniors
   - *Social Distance*: casual with team, diplomatic with external or unfamiliar
   - *Gravity of Situation*: urgent for critical technical debt, casual for nice-to-have
   - *Cultural Context*: frame as improvement, not criticism of previous work
   - *Medium*: chat for suggestions, formal proposal for large refactoring
   
   **Common Mistakes**:
   - Too insulting: "This is garbage code" (attacking previous work)
   - Not explaining why: Missing business case for refactoring time
   - Wrong timing: Suggesting big refactor right before deadline
   
   **Cultural Notes**: Refactoring can be sensitive. Respect original authors. Focus on evolution and improvement, not failure.
   
   **Context Examples**:
   - **Situation 1**: Team planning session → **Appropriate Variant**: Casual or Lively
   - **Situation 2**: Sprint planning → **Appropriate Variant**: Semi-Formal
   - **Situation 3**: Technical debt proposal → **Appropriate Variant**: Formal
