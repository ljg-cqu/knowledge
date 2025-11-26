# Rust Programming Vocabulary: Adjectives

1. **Adjective**: mutable (comp: more mutable, sup: most mutable)
   **Meaning**: 
   - (Programming) Capable of being changed or modified after initial creation; describes data that can be altered during program execution. (gradable, attributive/predicative)
   
   **Synonyms**: changeable, modifiable, variable, alterable, non-constant
   
   **Antonyms**: immutable, constant, fixed, unchangeable
   
   **When to Use**: Use when describing variables, references, or data structures that need to be modified after initialization in Rust code. Essential for explaining Rust's borrowing rules and ownership system.
   
   **When NOT to Use**: Avoid when describing constants, literals, or immutable references. Do not use in contexts where data safety through immutability is the goal.
   
   **Common Phrases**: 
   - mutable reference
   - mutable borrow
   - mutable variable
   - make something mutable
   - declare as mutable
   
   **Root Analysis**: mut(change) + able(capable of)
   
   **Etymology**: Latin mutabilis → English mutable (14th century), meaning "liable to change"
   
   **Examples [Casual]**: 
   - You need to add `mut` to make that variable mutable.
   - The function requires a mutable reference so it can update the value.
   
   **Examples [Formal]**: 
   - A mutable borrow allows modification of the borrowed value while maintaining memory safety guarantees.
   - The iterator provides mutable access to each element in the collection.

1. **Adjective**: generic (comp: more generic, sup: most generic)
   **Meaning**: 
   - (Programming) Not specific or specialized; applicable to multiple types through parametric polymorphism. (gradable, attributive/predicative)
   - *(Sense 2)* Using type parameters to write code that works with various concrete types.
   
   **Synonyms**: parametric, polymorphic, type-agnostic, universal, abstract
   
   **Antonyms**: specific, concrete, monomorphic, specialized
   
   **When to Use**: Use when describing functions, structs, enums, or traits that accept type parameters. Common in discussions of Rust's type system and reusable code patterns.
   
   **When NOT to Use**: Avoid when discussing monomorphized concrete implementations or when specificity is the focus.
   
   **Common Phrases**: 
   - generic function
   - generic type parameter
   - generic programming
   - generic implementation
   - generic constraint
   
   **Root Analysis**: gener(kind, class) + ic(relating to)
   
   **Etymology**: French générique → Latin genus (kind) (17th century)
   
   **Examples [Casual]**: 
   - We can make this generic so it works with any type.
   - Just add a generic parameter to the struct definition.
   
   **Examples [Formal]**: 
   - Generic functions enable code reuse while maintaining type safety through monomorphization.
   - The trait defines generic associated types that allow flexible implementations.

1. **Adjective**: unsafe (comp: more unsafe, sup: most unsafe)
   **Meaning**: 
   - (Programming) Not checked or guaranteed by Rust's safety mechanisms; requiring manual verification of correctness. (gradable, attributive)
   
   **Synonyms**: unchecked, unverified, raw, unguarded, unrestricted
   
   **Antonyms**: safe, checked, verified, guaranteed
   
   **When to Use**: Use when describing code blocks, functions, traits, or operations that bypass Rust's compile-time safety guarantees. Essential for FFI, raw pointers, and low-level operations.
   
   **When NOT to Use**: Avoid as a general criticism of code quality; it's a technical designation in Rust, not a judgement.
   
   **Common Phrases**: 
   - unsafe block
   - unsafe function
   - unsafe trait
   - unsafe code
   - unsafe operations
   
   **Root Analysis**: un(not) + safe(free from danger)
   
   **Etymology**: Old English unsæf (not safe), from un- + safe
   
   **Examples [Casual]**: 
   - You'll need an unsafe block to dereference that raw pointer.
   - The FFI calls are wrapped in unsafe because we can't verify them.
   
   **Examples [Formal]**: 
   - Unsafe code requires programmers to manually uphold invariants that the compiler cannot verify.
   - The unsafe trait implementation must guarantee thread safety without compiler assistance.

1. **Adjective**: asynchronous (comp: more asynchronous, sup: most asynchronous)
   **Meaning**: 
   - (Programming) Operating independently of a main program flow; not occurring at the same time; describes operations that don't block execution. (non-gradable, attributive)
   
   **Synonyms**: async, non-blocking, concurrent, deferred, future-based
   
   **Antonyms**: synchronous, blocking, sequential, immediate
   
   **When to Use**: Use when describing functions, operations, or programming models that allow concurrent execution without blocking. Common in async/await discussions.
   
   **When NOT to Use**: Avoid when describing parallel execution or when synchronous blocking behavior is intended.
   
   **Common Phrases**: 
   - asynchronous function
   - asynchronous runtime
   - asynchronous programming
   - asynchronous operation
   - asynchronous execution
   
   **Root Analysis**: a(not) + syn(together) + chron(time) + ous(adjective suffix)
   
   **Etymology**: Greek asunkhronos (not synchronous) → modern computing term (1950s)
   
   **Examples [Casual]**: 
   - Make that function asynchronous so it doesn't block the thread.
   - The async version runs much faster with multiple requests.
   
   **Examples [Formal]**: 
   - Asynchronous functions return futures that can be polled by the runtime executor.
   - The asynchronous I/O model enables efficient handling of concurrent operations.

1. **Adjective**: idiomatic (comp: more idiomatic, sup: most idiomatic)
   **Meaning**: 
   - (Programming) Following the conventional patterns, styles, and best practices of Rust; natural and appropriate to the language. (gradable, predicative)
   
   **Synonyms**: conventional, standard, Rust-like, canonical, typical
   
   **Antonyms**: unidiomatic, non-standard, foreign, awkward
   
   **When to Use**: Use when describing code that follows Rust best practices, conventions, and community standards. Important in code reviews and style discussions.
   
   **When NOT to Use**: Avoid when describing functionally correct but non-standard code that may still be acceptable in certain contexts.
   
   **Common Phrases**: 
   - idiomatic Rust
   - idiomatic pattern
   - idiomatic solution
   - write idiomatic code
   - idiomatic approach
   
   **Root Analysis**: idiom(characteristic mode) + atic(relating to)
   
   **Etymology**: Greek idiōmatikos → Latin idiomaticus (characteristic of a particular language)
   
   **Examples [Casual]**: 
   - That's not very idiomatic - you should use pattern matching instead.
   - Try to write more idiomatic Rust by using iterators.
   
   **Examples [Formal]**: 
   - Idiomatic Rust code leverages the type system and ownership model effectively.
   - The implementation follows idiomatic patterns recommended by the Rust community.

1. **Adjective**: thread-safe (non-gradable, attributive/predicative)
   **Meaning**: 
   - (Programming) Safe to use from multiple threads simultaneously without causing data races or undefined behavior. (non-gradable, attributive/predicative)
   
   **Synonyms**: concurrency-safe, multi-thread safe, synchronization-safe
   
   **Antonyms**: non-thread-safe, race-prone, unsafe for concurrency
   
   **When to Use**: Use when describing types, functions, or operations that can be safely shared or accessed across thread boundaries. Essential for concurrent programming discussions.
   
   **When NOT to Use**: Avoid when describing single-threaded contexts or when thread safety is not a concern.
   
   **Common Phrases**: 
   - thread-safe type
   - thread-safe implementation
   - ensure thread safety
   - thread-safe access
   - thread-safe wrapper
   
   **Root Analysis**: thread(execution context) + safe(free from danger)
   
   **Etymology**: Computing compound term from thread + safe (1990s)
   
   **Examples [Casual]**: 
   - This type is thread-safe, so you can share it between threads.
   - We need a thread-safe counter for the concurrent workers.
   
   **Examples [Formal]**: 
   - The Send and Sync traits guarantee thread-safe behavior at compile time.
   - Thread-safe abstractions prevent data races through Rust's type system.

1. **Adjective**: lifetimed (non-gradable, attributive)
   **Meaning**: 
   - (Programming) Associated with or annotated by a lifetime parameter; describes types or references that have explicit lifetime constraints. (non-gradable, attributive)
   
   **Synonyms**: lifetime-annotated, lifetime-bound, temporally-constrained
   
   **Antonyms**: lifetime-free, 'static, owned
   
   **When to Use**: Use when describing references, structs, or functions that require explicit lifetime annotations. Key for understanding borrow checker requirements.
   
   **When NOT to Use**: Avoid when describing owned types or static lifetimes where temporal constraints are implicit or unnecessary.
   
   **Common Phrases**: 
   - lifetimed reference
   - lifetimed struct
   - lifetimed parameter
   - lifetimed type
   - multiple lifetimed arguments
   
   **Root Analysis**: lifetime(duration of validity) + ed(possessing)
   
   **Etymology**: Modern Rust-specific compound (2010s) from lifetime + -ed
   
   **Examples [Casual]**: 
   - You need to add lifetime annotations to this lifetimed struct.
   - The function signature shows two lifetimed parameters.
   
   **Examples [Formal]**: 
   - Lifetimed references ensure memory safety by tracking data validity at compile time.
   - The API requires lifetimed types to express borrowing relationships explicitly.

1. **Adjective**: zero-cost (non-gradable, attributive)
   **Meaning**: 
   - (Programming) Having no runtime performance penalty; describes abstractions that compile to the same machine code as hand-written low-level equivalents. (non-gradable, attributive)
   
   **Synonyms**: overhead-free, performance-neutral, abstraction-free (at runtime), penalty-free
   
   **Antonyms**: overhead-heavy, costly, performance-impacting
   
   **When to Use**: Use when describing Rust abstractions, features, or patterns that don't sacrifice runtime performance. Central to Rust's design philosophy.
   
   **When NOT to Use**: Avoid when discussing abstractions that do have runtime costs or when compile-time costs are the focus.
   
   **Common Phrases**: 
   - zero-cost abstraction
   - zero-cost generics
   - zero-cost guarantee
   - zero-cost wrapper
   - zero-cost principle
   
   **Root Analysis**: zero(no amount) + cost(expense, overhead)
   
   **Etymology**: Computing philosophy term popularized by C++ and Rust (1990s-2010s)
   
   **Examples [Casual]**: 
   - Rust's iterators are zero-cost abstractions that compile down to tight loops.
   - Don't worry about using that wrapper - it's zero-cost.
   
   **Examples [Formal]**: 
   - Zero-cost abstractions enable expressive high-level code without sacrificing performance.
   - The language design prioritizes zero-cost principles throughout the standard library.

1. **Adjective**: borrowed (non-gradable, attributive)
   **Meaning**: 
   - (Programming) Temporarily accessed through a reference without transferring ownership; describes values accessed via Rust's borrowing mechanism. (non-gradable, attributive)
   
   **Synonyms**: referenced, temporarily-accessed, non-owned
   
   **Antonyms**: owned, moved, consumed
   
   **When to Use**: Use when describing values accessed through references rather than owned. Fundamental to Rust's ownership system and memory management.
   
   **When NOT to Use**: Avoid when describing owned values or when ownership has been transferred through moving.
   
   **Common Phrases**: 
   - borrowed value
   - borrowed reference
   - borrowed data
   - borrowed immutably
   - borrowed mutably
   
   **Root Analysis**: borrow(temporary use) + ed(past participle)
   
   **Etymology**: Old English borgian (to lend, to borrow) → specialized Rust meaning (2010s)
   
   **Examples [Casual]**: 
   - You can't move that value because it's currently borrowed.
   - The function takes a borrowed reference instead of owning the data.
   
   **Examples [Formal]**: 
   - Borrowed values must adhere to aliasing rules enforced by the borrow checker.
   - The API design favors borrowed parameters to enable flexible caller patterns.

1. **Adjective**: polymorphic (comp: more polymorphic, sup: most polymorphic)
   **Meaning**: 
   - (Programming) Capable of taking multiple forms; describes code that can work with different types through traits or generics. (gradable, attributive/predicative)
   
   **Synonyms**: multi-form, generic, adaptable, type-flexible, universal
   
   **Antonyms**: monomorphic, type-specific, concrete, inflexible
   
   **When to Use**: Use when describing functions, types, or behaviors that work with multiple types through trait bounds or dynamic dispatch. Key for abstraction discussions.
   
   **When NOT to Use**: Avoid when describing monomorphic concrete implementations or when type specificity is required.
   
   **Common Phrases**: 
   - polymorphic function
   - polymorphic behavior
   - polymorphic type
   - static polymorphism
   - dynamic polymorphism
   
   **Root Analysis**: poly(many) + morph(form) + ic(relating to)
   
   **Etymology**: Greek polumorphos (having many forms) → computing term (1960s)
   
   **Examples [Casual]**: 
   - Traits let you write polymorphic code that works with many types.
   - Use trait objects for runtime polymorphic dispatch.
   
   **Examples [Formal]**: 
   - Rust provides polymorphic abstraction through both static generics and dynamic trait objects.
   - The polymorphic interface enables uniform treatment of heterogeneous types.
