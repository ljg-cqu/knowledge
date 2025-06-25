Rust's Type System

Wed Jun 25 2025

### Overview of Rust's Type System

Rust is a modern systems programming language that stands out due to its strong and expressive type system, which is a cornerstone of its design philosophy. This type system is designed to provide robust safety guarantees and high performance, often eliminating the need for runtime checks in certain scenarios. It achieves this by performing extensive checks at compile time, which helps in catching a multitude of common programming errors early in the development process, such as uninitialized variables, invalid memory access, and data races. Rust's type system is static, meaning that types for all variables are determined and verified during compilation. This static typing ensures that type-related errors are identified before the program executes, contributing to greater reliability compared to dynamically typed languages where such errors are only discovered at runtime.

### Fundamental Types in Rust

Rust's type system is built upon a set of fundamental data types, broadly categorized into scalar and compound types. **Scalar types** represent a single value and include integers, floating-point numbers, Booleans, and characters. Integer types in Rust come in signed (e.g., `i8`, `i16`, `i32`, `i64`, `i128`) and unsigned (e.g., `u8`, `u16`, `u32`, `u64`, `u128`) variants, with sizes indicating the number of bits they occupy. Additionally, `isize` and `usize` are pointer-sized integer types whose bit length depends on the target platform's architecture (32 or 64 bits). Floating-point numbers are represented by `f32` (32-bit) and `f64` (64-bit) types, adhering to the IEEE-754 standard, with `f64` being the default for its precision and comparable speed on modern CPUs. The Boolean type, `bool`, can hold either `true` or `false` and occupies one byte of memory. The `char` type is four bytes in size and represents a Unicode Scalar Value, allowing for a wide range of characters beyond ASCII, including accented letters, Chinese, Japanese, Korean characters, and emojis.

**Compound types** are designed to group multiple values into a single type, enhancing data modeling and structure. Rust provides two primary primitive compound types: tuples and arrays. Tuples are fixed-size, heterogeneous collections, meaning they can store multiple values of different types. For example, a tuple can be declared as `let tuple_example: (i32, f64, bool) = (42, 3.14, true);`. Individual values within a tuple can be accessed through pattern matching (destructuring) or by their index using dot notation (e.g., `x.0`). Arrays, in contrast to tuples, are fixed-size, homogeneous collections, storing multiple values of the same type. An example is `let array_example: [i32; 5] = [1, 2, 3, 4, 5];`. Arrays are useful for stack allocation and when a fixed number of elements is guaranteed, though Rust's standard library also offers `Vec` for dynamically sized collections. Slices (`&[T]`) provide a dynamically sized view into a contiguous sequence of elements, typically part of an array or another slice, allowing work with a portion of data without copying it. Rust also differentiates between `String` (a growable, heap-allocated string) and `&str` (a string slice, often a reference to a `String` or a string literal).

### Ownership, Borrowing, and Lifetimes

Rust's type system is famously built around the concepts of **ownership**, **borrowing**, and **lifetimes**, which together guarantee memory and thread safety without the need for a garbage collector. These principles enable Rust to prevent common errors like dangling pointers, data races, buffer overflows, and accesses to uninitialized or deallocated memory at compile time.

**Ownership** dictates that every value in Rust has a single variable that acts as its owner. When the owner goes out of scope, the value is automatically deallocated (dropped), ensuring memory is freed predictably and safely. This "single owner" rule is closely related to linear types, preventing implicit duplication of values and ensuring that memory is deallocated exactly once.

**Borrowing** extends ownership by allowing references to values without transferring ownership. References can be either immutable (`&T`) or mutable (`&mut T`). Rust's strict rules for borrowing are enforced by the "borrow checker" at compile time: a value can have either one mutable reference or any number of immutable references at a given time, but not both simultaneously. This prevents data races and ensures that data cannot be unexpectedly modified while being read. For instance, trying to create multiple mutable references to a single value will result in a compile-time error.

**Lifetimes** are a crucial component that work with borrowing to ensure references are always valid and do not outlive the data they point to. Lifetimes are not runtime constructs but rather annotations that the Rust compiler uses to verify the validity of references at compile time. While the compiler often infers lifetimes automatically, programmers can explicitly provide lifetime annotations for more fine-grained control or when the compiler needs assistance in ambiguous situations. This static analysis prevents dangling references, which occur when a reference points to memory that has already been deallocated.

The combined effect of ownership, borrowing, and lifetimes allows Rust to offer memory safety guarantees comparable to languages with garbage collection, but with the performance characteristics of systems languages like C and C++.

### Type Inference

Rust features a sophisticated **type inference** mechanism that allows the compiler to automatically determine the type of a value based on the context in which it is used. This capability reduces the need for explicit type annotations, making the code more concise and easier to write while still maintaining strict type safety. For example, `let x = 5;` will cause the compiler to infer `x` as an `i32` by default. Similarly, `let my_float = 5.0;` will infer `my_float` as an `f64`.

Under the hood, Rust's type inference is based on the **Hindley-Milner algorithm**, which is extended to accommodate Rust's unique features, including subtyping, region (lifetime) inference, and higher-ranked types. The compiler builds an "inference context" populated with inference variables that represent unknown types or regions. These variables are then resolved by gathering constraints from the code and attempting to unify them. The process involves enforcing equality and subtyping relationships between types.

Despite its power, type inference has limitations. There are cases where the compiler cannot infer a type without an explicit type annotation, typically when generic parameters are involved and the concrete type cannot be determined from the context alone. In such situations, the compiler will issue an error, prompting the programmer to provide the necessary type information, such as `let guess: u32 = "42".parse().expect("Not a number!");` when parsing a string to an integer. For numeric literals, a type suffix can be used, like `10u8` or `10_u8`, to explicitly define the type.

### Traits

Rust's **trait system** is a fundamental mechanism for defining shared behavior across different types, analogous to interfaces in other programming languages. Traits allow developers to specify a set of methods that a type must implement to be considered a member of that trait, enabling polymorphism and abstracting common functionalities without relying on class inheritance.

A trait definition includes method signatures that describe the required behavior. Any concrete type can then `impl` (implement) this trait by providing the actual code for each method. For example, a `Shape` trait might define an `area` method, which both `Circle` and `Rectangle` structs would implement according to their specific area calculation logic. This allows functions to accept any type that implements a particular trait using `&dyn Trait` (trait objects), enabling runtime polymorphism.

Traits are crucial for Rust's generic programming, as they are used to define **trait bounds** on generic type parameters [27:1793, 4:Result 4]. These bounds constrain generic functions and data structures to work only with types that exhibit certain behaviors, ensuring type safety at compile time [4:Result 4]. Traits can also include **associated types**, which connect a type placeholder with the trait, allowing method signatures within the trait to use these placeholder types. Furthermore, traits can have default method implementations, which can be overridden by types that implement the trait. The trait system allows for extensive code reuse and robust abstraction, providing a powerful tool for structuring Rust programs.

### Generics

Generics in Rust are a powerful feature of its type system that allows developers to write flexible, reusable code definitions for items like function signatures, structs, enums, and traits. This means a single code block can operate on multiple different concrete data types, reducing code duplication while maintaining type safety and performance. Rust's approach to generics is based on **monomorphization**, where the compiler generates specialized versions of generic code for each concrete type used at compile time [4:Result 4, 44:1810]. This strategy ensures that there is no runtime overhead associated with generics, providing "zero-cost abstractions" and performance comparable to C/C++.

The power of generics is significantly enhanced by their integration with Rust's **trait system** [4:Result 4]. Generic type parameters are often constrained by **trait bounds**, which specify the required behavior and capabilities of the types that can be substituted for the generic parameter [4:Result 4]. For instance, a generic function `fn largest<T: PartialOrd>(list: &[T]) -> T` indicates that `T` must implement the `PartialOrd` trait, allowing comparisons to be made on elements of any type `T` that supports it [4:Result 4]. This ensures that generic code is only used with types that adhere to a specific contract, guaranteeing type safety and correctness at compile time [4:Result 4].

Generics, combined with Rust's ownership and borrowing rules, contribute significantly to memory safety [4:Result 4]. The compiler can perform rigorous checks on generic code, preventing common errors such as dangling pointers and data races, without relying on a garbage collector [4:Result 4]. This makes generics an essential tool for building efficient, safe, and reusable abstractions in systems programming, distinguishing Rust from traditional object-oriented languages that might use inheritance or dynamic dispatch for similar flexibility [4:Result 4].

### Custom Type Definitions

Rust provides robust mechanisms for defining custom data types, primarily through **structs**, **enums**, and **type aliases**, enabling developers to model complex data structures and improve code organization [11:815, 6:Result 6].

**Structs** (structures) are used to create custom types that group related data together. They come in three forms:
*   **Classic C Structs** have named fields, allowing for clear and organized data representation. For example, a `Point` struct could have `x`, `y`, and `z` fields of type `i64`.
*   **Tuple Structs** are similar to tuples but have a defined name for the overall type. They have unnamed fields that are accessed by index. For instance, `struct Color(i32, i32, i32)` defines a `Color` type that groups three `i32` values [6:459, 6:Result 6, 18:1667].
*   **Unit Structs** are structs that hold no values. They are primarily used when a type is needed for trait implementation but no data needs to be stored within the type itself [6:Result 6, 18:1667].

**Enums** (enumerations) allow defining a type by listing its possible discrete variants. Rust's enums are particularly powerful, akin to **algebraic data types** found in functional programming languages, as their variants can carry associated data. This associated data can be named (like fields in a struct), unnamed (like elements in a tuple), or absent (unit-like). For example, an `HttpRequest` enum might have variants like `Get(String)` for a URL, or `Post { url: String, body: String }` to include both a URL and a request body. This flexibility, combined with Rust's powerful **pattern matching** (`match` expressions), makes enums highly effective for expressive and safe data modeling and control flow. Common examples from the standard library include `Option<T>` (which can be `Some(T)` or `None` for optional values) and `Result<T, E>` (which can be `Ok(T)` for success or `Err(E)` for failure).

**Type aliases** provide a new name for an existing type using the `type` keyword [6:Result 6]. They are primarily used to simplify complex type signatures or to improve code readability by giving a more descriptive name to an existing type, such as `type Kilometers = i32;` [6:Result 6]. Unlike structs or enums, type aliases do not create new, distinct types but merely provide a synonym, meaning they do not offer additional type safety beyond the underlying type [35:1801, 6:Result 6]. However, the "New Type Idiom," which involves wrapping a single item in a tuple struct (e.g., `struct MyId(u32);`), can be used to create a "strong" or "distinct" type, providing more type safety than a simple alias.

### Type Conversions and Coercions

Rust's type system is designed with a strong emphasis on explicitness and safety, particularly concerning type conversions and coercions [15:1285, 7:Result 7]. Unlike some dynamically typed languages that perform implicit type conversions (e.g., JavaScript converting a string to a number for arithmetic operations), Rust generally requires **explicit type conversion**.

Explicit conversions can be achieved through several mechanisms:
*   The `as` keyword: This is used for safe casts between primitive numeric types, such as converting a `f64` to an `i64` (`let integer = number as i64;`). The `as` keyword can also be used for certain pointer conversions, though dereferencing raw pointers requires `unsafe` blocks.
*   Methods like `parse()`: The `parse()` method, available on `&str` types, can convert strings into any type that implements the `std::str::FromStr` trait. This method returns a `Result` type, necessitating explicit error handling. Programmers can also implement the `FromStr` trait for their custom types to enable string parsing.
*   Standard library traits: Rust provides traits like `From` and `Into` for general-purpose type conversions, as well as `TryFrom` and `TryInto` for infallible and fallible conversions, respectively [15:1375, 7:Result 7]. Many other conversion methods are available throughout the standard library and third-party crates, often following `to_` or `from_` naming conventions (e.g., `to_string()`, `from_str()`).

**Implicit coercions** in Rust are highly restricted and occur only at specific "coercion sites" within the code, such as `let` statements where an explicit type is given, function arguments, field instantiations, and function return values. These limited coercions are designed to simplify common scenarios without introducing ambiguity or unsafety. A typical example is the automatic conversion of a mutable reference (`&mut T`) to an immutable reference (`&T`). Additionally, the dot operator can perform auto-dereferencing and auto-referencing to make types match in method calls or field accesses. While useful for ergonomics, these implicit coercions are tightly controlled by the compiler and are not a general mechanism for converting between unrelated types.

Rust's strictness in type conversion prevents many runtime errors that might arise from unintended implicit conversions in other languages, ensuring that type changes are either explicitly requested by the programmer or occur in well-defined, safe contexts.

### Error Handling with Option and Result Types

Rust's type system profoundly influences how errors are handled, primarily through the use of the `Option` and `Result` enums [13:1083, 10:575, 8:Result 8]. These types enforce explicit error management, making potential failures part of a function's signature and preventing them from being ignored or overlooked [10:710, 17:1583, 8:Result 8].

The `Option` type is an enumeration with two variants: `Some(T)`, which indicates the presence of a value of type `T`, and `None`, which signifies the absence of a value. This design eliminates the concept of null references, a common source of bugs in many other languages, by requiring explicit handling of cases where a value might not exist [13:1082, 5:Result 5]. For instance, a function that attempts to find the length of a string might return `Option<usize>`, where `None` indicates no string was found. Programmers must explicitly `match` on the `Option` or use methods like `if let` to safely unwrap the value or handle its absence. The `?` operator provides a concise way to propagate a `None` value up the call stack if a function returns an `Option`. While `unwrap()` and `expect()` methods can be used to retrieve the value directly, they will cause the program to `panic!` (exit with an error) if a `None` variant is encountered, making their use generally discouraged in production code where robust error handling is required.

The `Result` type is also an enumeration, used specifically for recoverable errors, and has two variants: `Ok(T)`, representing a successful operation with a value of type `T`, and `Err(E)`, indicating a failed operation with an error value of type `E`. This type forces developers to acknowledge and manage potential failure points within their code explicitly. A common use case is for functions that might fail, such as dividing by zero, where the function would return `Err("Cannot divide by zero".to_string())` instead of a numeric result. Similar to `Option`, `Result` values are typically handled using `match` statements to execute different logic for success and error cases. The `if let` construct can also be used when only the `Ok` case is of interest. The `?` operator is particularly useful for propagating `Err` values, simplifying error handling chains by automatically returning the error if an operation fails. Best practices for using `Result` include defining custom error types for better organization and avoiding excessive use of `unwrap()` or `expect()` to prevent panics.

By embedding optionality and error handling directly into the type system, Rust ensures that programmers must confront and address all possible outcomes, leading to more resilient and maintainable applications.

### Impact and Usability of Rust's Type System

Rust's type system, with its unique features like ownership, borrowing, and lifetimes, aims to deliver strong safety and performance guarantees. It ensures memory safety by statically guaranteeing the absence of null or dangling references and preventing data races at compile time without relying on a garbage collector [7:477, 5:Result 5]. This rigorous compile-time checking allows Rust programs to achieve performance levels similar to C and C++ while significantly reducing common classes of bugs. The system also enables flexible and expressive data modeling through features like algebraic data types (enums and structs) and traits, which define shared behavior and facilitate code reuse through generics [2:16, 2:45, 26:1792, 4:Result 4].

Despite these significant benefits, Rust's advanced type system presents a steep learning curve, especially concerning its ownership, borrowing, and lifetime rules. Studies indicate that the borrow checker, which enforces these rules, is often cited as the biggest challenge in learning Rust and requires a fundamental shift in programming paradigms. Even experienced Rust developers may struggle with complex lifetime computations, leading to difficulties in understanding and resolving compiler errors. The diagnostic messages from the compiler, while generally helpful, can become less informative when dealing with highly complex trait interactions or subtle borrow checker issues, sometimes leading to frustration.

However, the perceived difficulty is often outweighed by the benefits of writing safe, high-performance, and reliable code. Rust's tooling, strong community support, and its promise of safety without sacrificing speed make it a popular choice, particularly for systems programming, embedded programs, and safety-critical applications. The type system's ability to enforce correct I/O interface configuration and ensure operations are performed only on correctly configured peripherals further highlights its utility in critical domains.

The following table provides a high-level comparison of Rust's type system characteristics with those of C and Python, as outlined in one of the documents:

| Property         | C               | Python          | Rust            |
| :--------------- | :-------------- | :-------------- | :-------------- |
| Type-safe?       | No (Weak, Static) | No (Strong, Dynamic) | Yes (Strong, Static) |
| Memory-safe?     | No              | Yes             | Yes             |
| Fast?            | Yes             | No              | Yes             |

This comparison underscores Rust's position in offering both strong type and memory safety guarantees, which are typically associated with higher-level languages, while maintaining the performance expected of systems programming languages.

Bibliography
0401-coercions - The Rust RFC Book. (2014). https://rust-lang.github.io/rfcs/0401-coercions.html

A Burtsev, D Appel, D Detweiler, T Huang, & Z Li. (2021). Isolation in Rust: What is Missing? https://dl.acm.org/doi/abs/10.1145/3477113.3487272

A. Light, T. Doeppner, & S. Krishnamurthi. (2015). Reenix: Implementing a Unix-Like Operating System in Rust. https://www.semanticscholar.org/paper/a0a6e98fec17d417741981f3797c2b741d3024e5

Advanced Traits - The Rust Programming Language. (2024). https://doc.rust-lang.org/book/ch20-02-advanced-traits.html

Can I define my own “strong” type alias in Rust? - Stack Overflow. (2021). https://stackoverflow.com/questions/69443534/can-i-define-my-own-strong-type-alias-in-rust

Code Reuse in Rust - GitHub Gist. (2020). https://gist.github.com/qinwf/55f651daece54a6fdfa2

Custom Types - Rust By Example. (n.d.). https://doc.rust-lang.org/rust-by-example/custom_types.html

Data Types - The Rust Programming Language. (2021). https://doc.rust-lang.org/book/ch03-02-data-types.html

David Blaser, Dr. Peter Müller, F. Poli, & Vytautas Astrauskas. (2019). Simple Visualization of Lifetime Errors in Rust. https://www.semanticscholar.org/paper/8c357f708913c10f7c2bd441f067e0239e5a252f

David J. Pearce. (2021). A Lightweight Formalism for Reference Lifetimes and Borrowing in Rust. In ACM Transactions on Programming Languages and Systems (TOPLAS). https://dl.acm.org/doi/10.1145/3443420

Error Handling - The Rust Programming Language. (2018). https://doc.rust-lang.org/book/ch09-00-error-handling.html

Fundamentals: Type Systems - High Assurance Rust: Developing ... (2012). https://highassurance.rs/chp16_appendix/types.html

Gavin Gray & Will Crichton. (2023). Debugging Trait Errors as Logic Programs. In ArXiv. https://arxiv.org/abs/2309.05137

Generic Data Types - The Rust Programming Language. (2021). https://doc.rust-lang.org/book/ch10-01-syntax.html

Generic Types, Traits, and Lifetimes - The Rust Programming ... (2024). https://doc.rust-lang.org/book/ch10-00-generics.html

How does type inference work? - Rust Users Forum. (2024). https://users.rust-lang.org/t/how-does-type-inference-work/108438

How to perform type conversion in Rust - Educative.io. (n.d.). https://www.educative.io/answers/how-to-perform-type-conversion-in-rust

J. Bhattacharjee. (2019). Using Rust Applications. https://link.springer.com/chapter/10.1007/978-1-4842-5121-8_8

J Hong & S Ryu. (2024). Don’t Write, but Return: Replacing Output Parameters with Algebraic Data Types in C-to-Rust Translation. In Proceedings of the ACM on Programming Languages. https://dl.acm.org/doi/abs/10.1145/3656406

Jakob Beckmann, Eth Zürich, F. Poli, Christoph Matheja Prof. Peter, & Müller. (2020). Verifying Safe Clients of Unsafe Code and Trait Implementations in Rust. https://www.semanticscholar.org/paper/417738a0b6b1e2772bd3947e5d53cabbd8e6033a

Kasra Ferdowsi. (2023). The Usability of Advanced Type Systems: Rust as a Case Study. In ArXiv. https://arxiv.org/abs/2301.02308

Lennard Gäher, Michael Sammler, Ralf Jung, Robbert Krebbers, & Derek Dreyer. (2024). RefinedRust: A Type System for High-Assurance Verification of Rust Programs. In Proceedings of the ACM on Programming Languages. https://dl.acm.org/doi/10.1145/3656422

Leo Osvald & Tiark Rompf. (2017). Rust-like borrowing with 2nd-class values (short paper). In Proceedings of the 8th ACM SIGPLAN International Symposium on Scala. https://dl.acm.org/doi/10.1145/3136000.3136010

M Depta. (n.d.). Analysis of Type–Driven approach to systems programming: Implementation of OpenGL library for Rust. https://wmi.uwr.edu.pl/wp-content/uploads/sites/288/2024/12/Depta-Mikolaj-praca.pdf

M Emre, P Boyland, A Parekh, & R Schroeder. (2023). Aliasing limits on translating C to safe Rust. https://dl.acm.org/doi/abs/10.1145/3586046

Mastering Generics in Rust: A Hands-on Guide - LinkedIn. (2023). https://www.linkedin.com/pulse/mastering-generics-rust-hands-onguide-luis-soares-m-sc-

Max Meldrum. (2018). Rust: Powered by Ownership. https://www.semanticscholar.org/paper/ef1a3229d39feb31ec4c94a71c95909d4bbc3e13

Michael Sproul. (2015). Implementing a Generic Radix Trie in Rust. https://www.semanticscholar.org/paper/a2938366de781e49c821bf2c378f7bfb49faba1d

Mihnea Dobrescu-Balaur & L. Negreanu. (2017). Enhancing RUSTDOC to Allow Search by Types. https://www.semanticscholar.org/paper/d6e350aaa23ebd4d1c896691a74f568b5219bcd1

Nicholas D. Matsakis & Felix S. Klock. (2014). The rust language. In HILT ’14. https://www.semanticscholar.org/paper/50eba68089cf51323d95631c2f59ff916848863f

O. Kiselyov, S. Jones, & Chung-chieh Shan. (2010). Fun with Type Functions. In Reflections on the Work of C. A. R. Hoare. https://www.semanticscholar.org/paper/8dd2c7c64451e6dda5d72351ef5c75d091352e05

P. Ashenden & Jim Lewis. (2008). Type System Changes. https://linkinghub.elsevier.com/retrieve/pii/B9780123742490500045

References and Borrowing - The Rust Programming Language. (2021). https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html

Rust by Example: Traits. (2020). https://rustbyexample.io/traits

Rust error handling is perfect actually - Bitfield Consulting. (2024). https://bitfieldconsulting.com/posts/rust-errors-option-result

Rust Powerful Type System. | Giuseppe Albrizio | Rustified - Medium. (2023). https://medium.com/bridging-the-gap-between-node-js-and-rust/rust-powerful-type-system-54b9e32b7425

Rust Type System: Making complex things simple. · swaits.com. (2023). https://swaits.com/beautiful-experience-with-rust-static-type-system/

Rust Using Rustlings — Part 7: Enums - Medium. (2023). https://medium.com/@verbruggenjesse/rust-using-rustlings-part-7-enums-7fb9f9cbbe5c

Rust’s Result Type: Error Handling Made Easy | by Leapcell - Medium. (2025). https://leapcell.medium.com/rusts-result-type-error-handling-made-easy-3e7a3b038214

Rust’s Type System: Exploring Type Inference, Phantom Data, and ... (2023). https://codedamn.com/news/rust/rusts-type-system-exploring-type-inference-phantom-data-associated-types

S Hamer, N Imtiaz, M Tamanna, & P Shabrina. (2024). Trusting code in the wild: Exploring contributor reputation measures to review dependencies in the Rust ecosystem. https://arxiv.org/abs/2406.10317

Static Guarantees - The Embedded Rust Book. (n.d.). https://docs.rust-embedded.org/book/static-guarantees/

Trait in Rust Explained: From Basics to Advanced Usage | by Leapcell. (2025). https://leapcell.medium.com/trait-in-rust-explained-from-basics-to-advanced-usage-0ddddf36333d

Type inference - Easy Rust. (n.d.). https://dhghomon.github.io/easy_rust/Chapter_8.html

Type inference - Rust Compiler Development Guide. (2017). https://rustc-dev-guide.rust-lang.org/type-inference.html

Understanding and Implementing Rust’s Option and Result Types. (2023). https://reintech.io/blog/understanding-implementing-rust-option-result-types

Understanding and Working with Rust’s Type System | Reintech media. (2023). https://reintech.io/blog/understanding-working-with-rust-type-system

Understanding Enums in Rust - Stack Overflow. (2022). https://stackoverflow.com/questions/70844636/understanding-enums-in-rust

V Astrauskas, P Müller, & F Poli. (2019). Leveraging Rust types for modular specification and verification. https://dl.acm.org/doi/abs/10.1145/3360573

Vytautas Astrauskas, Peter Müller, & F. Poli. (2021). Internship proposal: Formal veri(cid:28)cation of Rust programs. https://www.semanticscholar.org/paper/de3ed3ce51f08b4b218175433b58f2ca26628d19

Zhiqing Li, Xiaodong Hu, Zhu Min, Xing Yang, & Songgan Wen. (2015). Effect and Impact on Performance of Concrete of Migration Type Rust Inhibitor. https://www.semanticscholar.org/paper/51d176ec4d10b9de209a43a7b26bf7815235251c

何剑锋, 宋永良, 王家丰, & 王瑜玲. (2010). Composite type reinforced concrete rust inhibitor. https://www.semanticscholar.org/paper/a982ead6223877b66e2144cc2b15397c5ad50ff8



Generated by Liner
https://getliner.com/search/s/5926611/t/85971253