# Multi-Word Expressions Vocabulary - Perplexity

1. **Expression**: compile time (collocation - noun + noun)
   **Meaning**: 
   - The phase when source code is translated into executable code by a compiler
   - *Fixedness*: strong (always paired in this order)
   
   **Synonyms**: compilation phase, build time, translation time
   
   **Antonyms**: runtime, execution time
   
   **When to Use**: Programming contexts distinguishing from runtime behavior
   
   **When NOT to Use**: When referring to duration (use "compilation duration")
   
   **Common Variations**: 
   - compile-time (hyphenated adjective form)
   - at compile time (prepositional phrase)
   
   **Why This Partnership**: 
   - *For collocations*: Standard technical terminology in programming; "compile" always modifies "time" to specify when compilation occurs
   
   **Root Analysis**: compile (Latin compilare) + time (Old English tima)
   
   **Examples [Casual]**: 
   - The error shows up at compile time, not when running.
   - Compile time is when the code gets translated to machine language.
   
   **Examples [Formal]**: 
   - Rust enforces memory safety guarantees at compile time without runtime overhead.
   - Compile-time verification eliminates entire classes of runtime errors.

1. **Expression**: memory safety (collocation - noun + noun)
   **Meaning**: 
   - The state of preventing programs from accessing invalid memory locations
   - Protection against buffer overflows, use-after-free, and null pointer dereferences
   - *Fixedness*: strong (standard technical term)
   
   **Synonyms**: memory protection, safe memory management, memory security
   
   **Antonyms**: memory vulnerabilities, unsafe memory access
   
   **When to Use**: Systems programming, security discussions, language design contexts
   
   **When NOT to Use**: General computing contexts where "security" alone suffices
   
   **Common Variations**: 
   - memory-safe (adjective)
   - memory safe (predicative adjective)
   - memory safety guarantees (extended collocation)
   
   **Why This Partnership**: 
   - *For collocations*: "Safety" specifically modifies "memory" in security contexts; established term in programming language design
   
   **Root Analysis**: memory (Latin memoria) + safety (Old English sǣfþ)
   
   **Examples [Casual]**: 
   - Rust is all about memory safety - preventing crashes from bad pointers.
   - Memory safety bugs are the cause of most security vulnerabilities.
   
   **Examples [Formal]**: 
   - Rust achieves memory safety without garbage collection through compile-time ownership verification.
   - Memory safety violations constitute 70% of critical vulnerabilities in systems software.

1. **Expression**: borrow checker (collocation - noun + noun)
   **Meaning**: 
   - Rust's compile-time analysis system that enforces ownership and borrowing rules
   - *Fixedness*: strong (Rust-specific technical term)
   
   **Synonyms**: borrowing analyzer, reference validator, ownership enforcer
   
   **Antonyms**: (no direct antonyms - unique to Rust)
   
   **When to Use**: Rust programming contexts discussing compilation or type system
   
   **When NOT to Use**: Other programming languages (concept doesn't exist)
   
   **Common Variations**: 
   - the borrow checker (definite article typically used)
   - borrow checking (gerund form)
   - borrow-checker (hyphenated variant)
   
   **Why This Partnership**: 
   - *For collocations*: "Checker" performs action on "borrows"; coined term specific to Rust's design
   
   **Root Analysis**: borrow (Old English borgian) + checker (check + -er agent suffix)
   
   **Examples [Casual]**: 
   - The borrow checker is rejecting my code again - need to refactor.
   - Fighting the borrow checker is part of learning Rust.
   
   **Examples [Formal]**: 
   - The borrow checker performs flow-sensitive static analysis to prevent data races.
   - Developers struggle with borrow checker errors during initial Rust adoption.

1. **Expression**: zero-cost abstraction (collocation - adjective + noun + noun)
   **Meaning**: 
   - High-level programming constructs that compile to code as efficient as hand-written low-level code
   - *Fixedness*: strong (design principle in systems programming)
   
   **Synonyms**: zero-overhead abstraction, cost-free abstraction, efficient abstraction
   
   **Antonyms**: runtime overhead, abstraction penalty
   
   **When to Use**: Programming language design, performance discussions
   
   **When NOT to Use**: Business contexts (different meaning of "cost")
   
   **Common Variations**: 
   - zero-cost abstractions (plural)
   - zero cost abstraction (unhyphenated)
   - zero-cost principle
   
   **Why This Partnership**: 
   - *For collocations*: C++ design principle adopted by Rust; "zero-cost" modifies "abstraction" to emphasize no performance penalty
   
   **Root Analysis**: zero + cost + abstract + -ion
   
   **Examples [Casual]**: 
   - Zero-cost abstractions mean you don't pay performance penalties for cleaner code.
   - The iterator is a zero-cost abstraction - compiles to a simple loop.
   
   **Examples [Formal]**: 
   - Rust's zero-cost abstraction principle ensures high-level code compiles to optimal machine code.
   - Monomorphization enables zero-cost abstractions by generating specialized implementations.

1. **Expression**: type system (collocation - noun + noun)
   **Meaning**: 
   - The formal system that assigns types to program elements and enforces rules
   - A classification system for data and operations in programming
   - *Fixedness*: strong (standard PL theory term)
   
   **Synonyms**: typing system, type scheme, type theory
   
   **Antonyms**: untyped system, dynamic typing (context-dependent)
   
   **When to Use**: Programming language theory, compiler design discussions
   
   **When NOT to Use**: Casual programming contexts where "types" alone suffices
   
   **Common Variations**: 
   - type systems (plural)
   - advanced type system
   - static type system
   
   **Why This Partnership**: 
   - *For collocations*: "System" indicates organized rules governing "types"; foundational term in programming language theory
   
   **Root Analysis**: type (Greek typos) + system (Greek systema)
   
   **Examples [Casual]**: 
   - The type system catches errors before you run the code.
   - Rust's type system is strict but helps prevent bugs.
   
   **Examples [Formal]**: 
   - Rust encodes resource management rules directly into the type system.
   - The type system performs static verification of ownership invariants.

1. **Expression**: data race (collocation - noun + noun)
   **Meaning**: 
   - Concurrent access to shared data where at least one access is a write and accesses are not synchronized
   - *Fixedness*: strong (standard concurrency term)
   
   **Synonyms**: race condition (broader term), concurrent conflict, synchronization error
   
   **Antonyms**: synchronized access, thread-safe access
   
   **When to Use**: Concurrent programming, threading discussions, synchronization contexts
   
   **When NOT to Use**: Sequential programs (concept doesn't apply)
   
   **Common Variations**: 
   - data races (plural)
   - data-race (hyphenated)
   - race condition (related but broader term)
   
   **Why This Partnership**: 
   - *For collocations*: "Race" describes timing conflict over "data"; precise technical term in concurrent programming
   
   **Root Analysis**: data (Latin datum) + race (Old Norse rás)
   
   **Examples [Casual]**: 
   - Data races are nasty bugs - they only happen sometimes and are hard to debug.
   - Proper locking prevents data races between threads.
   
   **Examples [Formal]**: 
   - Rust prevents data races at compile time through strict borrowing rules.
   - Data races occur when mutable state is accessed from multiple threads without synchronization.

1. **Expression**: learning curve (collocation - noun + noun)
   **Meaning**: 
   - The rate at which proficiency is gained when learning a new skill
   - A graphical representation of progress over time
   - *Fixedness*: strong (standard educational/training term)
   
   **Synonyms**: proficiency trajectory, acquisition rate, mastery path
   
   **Antonyms**: (no direct antonyms - descriptive term)
   
   **When to Use**: Educational contexts, skill acquisition discussions, adoption planning
   
   **When NOT to Use**: Describing actual curved lines (use "curve" alone)
   
   **Common Variations**: 
   - steep learning curve (common modification)
   - gentle learning curve
   - learning curves (plural)
   
   **Why This Partnership**: 
   - *For collocations*: "Curve" graphically represents progress in "learning"; established metaphor in education and training
   
   **Root Analysis**: learning (Old English leornian + -ing) + curve (Latin curvus)
   
   **Examples [Casual]**: 
   - The learning curve is brutal - took me months to feel comfortable.
   - Once you get past the learning curve, it's much easier.
   
   **Examples [Formal]**: 
   - Rust's steep learning curve constitutes the primary adoption barrier for organizations.
   - The learning curve typically extends 3-6 months before developers achieve proficiency.

1. **Expression**: garbage collection (collocation - noun + noun)
   **Meaning**: 
   - Automatic memory management that reclaims memory no longer in use
   - *Fixedness*: strong (standard programming term)
   
   **Synonyms**: automatic memory management, GC, memory reclamation
   
   **Antonyms**: manual memory management, explicit deallocation
   
   **When to Use**: Programming language design, memory management discussions
   
   **When NOT to Use**: Waste management contexts (use "waste collection")
   
   **Common Variations**: 
   - garbage collector (agent noun)
   - GC (abbreviation)
   - garbage-collected (adjective)
   
   **Why This Partnership**: 
   - *For collocations*: "Collection" describes automatic gathering of "garbage" (unused memory); coined in early CS
   
   **Root Analysis**: garbage (unknown origin) + collection (Latin collectio)
   
   **Examples [Casual]**: 
   - Languages with garbage collection automatically free unused memory.
   - Garbage collection pauses can cause performance hiccups.
   
   **Examples [Formal]**: 
   - Rust achieves memory safety without garbage collection overhead.
   - Garbage collection introduces non-deterministic pauses unacceptable in real-time systems.

1. **Expression**: ownership model (collocation - noun + noun)
   **Meaning**: 
   - Rust's system for managing memory through single ownership and borrowing
   - A conceptual framework for resource management
   - *Fixedness*: strong (Rust-specific paradigm)
   
   **Synonyms**: ownership system, resource management model, memory model
   
   **Antonyms**: shared ownership, garbage-collected model
   
   **When to Use**: Rust programming contexts, memory management discussions
   
   **When NOT to Use**: Business contexts (different meaning of "ownership")
   
   **Common Variations**: 
   - ownership-based model
   - Rust's ownership model
   - ownership and borrowing model (extended)
   
   **Why This Partnership**: 
   - *For collocations*: "Model" describes conceptual framework for "ownership"; central to Rust's design philosophy
   
   **Root Analysis**: ownership (owner + -ship) + model (Latin modulus)
   
   **Examples [Casual]**: 
   - The ownership model takes getting used to, but prevents so many bugs.
   - You need to understand the ownership model before async makes sense.
   
   **Examples [Formal]**: 
   - Rust's ownership model replaces runtime garbage collection with compile-time verification.
   - The ownership model enforces single-owner semantics with temporary borrowing.

1. **Expression**: static analysis (collocation - adjective + noun)
   **Meaning**: 
   - Examination of program code without executing it, typically at compile time
   - *Fixedness*: strong (standard software engineering term)
   
   **Synonyms**: compile-time analysis, code analysis, program verification
   
   **Antonyms**: dynamic analysis, runtime analysis
   
   **When to Use**: Compiler design, code quality tools, security verification
   
   **When NOT to Use**: Runtime debugging (use "dynamic analysis")
   
   **Common Variations**: 
   - static analyzer (tool)
   - static analysis tools
   - flow-sensitive static analysis (extended)
   
   **Why This Partnership**: 
   - *For collocations*: "Static" (compile-time) modifies "analysis" to distinguish from dynamic/runtime analysis
   
   **Root Analysis**: static (Greek statikos) + analysis (Greek analusis)
   
   **Examples [Casual]**: 
   - Static analysis caught the bug before I even ran the code.
   - Tools like clippy do static analysis to suggest improvements.
   
   **Examples [Formal]**: 
   - The borrow checker performs flow-sensitive static analysis at compile time.
   - Static analysis eliminates runtime checks by verifying properties before execution.
