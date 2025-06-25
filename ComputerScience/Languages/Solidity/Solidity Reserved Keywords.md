Solidity Reserved Keywords

Wed Jun 25 2025

### Understanding Solidity Reserved Keywords

Reserved keywords in Solidity are specific words that possess predefined functions or meanings within the language's syntax and cannot be utilized as identifiers for variables, functions, or other custom names. These keywords are integral to the language's structure, enabling developers to write logical programming constructs for smart contracts on the Ethereum Virtual Machine (EVM). Their reservation prevents ambiguity and ensures the correct parsing and compilation of Solidity code.

### Comprehensive List of Reserved Keywords

Solidity differentiates between two categories of keywords: those that are strictly reserved for potential future use or to prevent identifier conflicts, and those that are fundamental to the language's current syntax and have specific functional roles.

**Strictly Reserved Keywords:** These keywords are set aside and should not be used as identifiers at all, as they might be integrated into the language's syntax in subsequent versions. Misusing them will result in compilation errors. The list includes:
*   `abstract`
*   `after`
*   `alias`
*   `apply`
*   `auto`
*   `byte`
*   `case`
*   `catch`
*   `copyof`
*   `default`
*   `define`
*   `final`
*   `immutable`
*   `implements`
*   `in`
*   `inline`
*   `let`
*   `macro`
*   `match`
*   `mutable`
*   `null`
*   `of`
*   `partial`
*   `promise`
*   `reference`
*   `relocatable`
*   `sealed`
*   `sizeof`
*   `static`
*   `supports`
*   `switch`
*   `try`
*   `typedef`
*   `typeof`
*   `unchecked`
*   `var`

**Common Solidity Keywords:** These words have designated roles in the Solidity syntax and are used for declaring types, controlling program flow, defining functions, and more. While they are not on the "strictly reserved" list for future use, they also cannot be used as general identifiers because they already have specific meanings. Examples include:
*   `address`
*   `assembly`
*   `bool`
*   `break`
*   `bytes`
*   `constant`
*   `contract`
*   `enum`
*   `event`
*   `external`
*   `fallback`
*   `function`
*   `if`
*   `internal`
*   `mapping`
*   `modifier`
*   `new`
*   `override`
*   `payable`
*   `pragma`
*   `private`
*   `public`
*   `pure`
*   `require`
*   `return`
*   `revert`
*   `struct`
*   `super`
*   `this`
*   `view`
*   `while`

### Restrictions and Usage of Keywords

Solidity's keywords are subject to strict usage rules to maintain code integrity and prevent syntactic errors. The most fundamental restriction is that **none of the reserved keywords can be used as variable names or function names**. For instance, attempting to name a variable `break` or `boolean` will lead to invalid code. If a developer attempts to use a reserved keyword as an identifier, the Solidity compiler will produce a `ParserError`, indicating that it expected an identifier but encountered a reserved keyword, and the code will fail to compile.

Beyond the general restriction against using keywords as identifiers, many common Solidity keywords have specific contextual uses:

*   **`pragma`**: This keyword is used at the beginning of a Solidity file to specify the compiler version the contract should be compiled with, such as `pragma solidity ^0.8.0;`.
*   **`contract`**: This defines a smart contract, which is a collection of code (functions) and data (state) residing on the Ethereum blockchain.
*   **`function`**: Used to define reusable blocks of code. Functions can take parameters and return values.
*   **Visibility Keywords (`public`, `private`, `internal`, `external`)**: These control the accessibility of state variables and functions.
    *   `public` variables and functions are accessible internally and externally, with an automatic getter function generated for public state variables.
    *   `private` variables and functions are only accessible from within the current contract.
    *   `internal` variables and functions can be accessed from the current contract or contracts derived from it.
    *   `external` functions can only be called from outside the contract.
*   **State Modifiers (`view`, `pure`, `payable`)**: These keywords modify the behavior of functions related to state changes or Ether transfers.
    *   `view` functions guarantee they will not modify the contract's state but can read it.
    *   `pure` functions ensure they neither read nor modify the state.
    *   `payable` functions can receive Ether during a transaction.
*   **`modifier`**: Used to define code that can be reused to change the behavior of functions, often for prerequisites like access control.
*   **`struct`**: Used to define custom data types that group together variables of different types, similar to records.
*   **`mapping`**: Creates key-value pair data structures, similar to hash tables or dictionaries.
*   **`enum`**: Restricts a variable to a predefined list of values.
*   **`require`**: Used for validating conditions and reverting transactions if the condition is not met, typically for malformed input or external component errors.
*   **`revert`**: Immediately stops execution and reverts all state changes, optionally with an explanatory string.
*   **`break`**: Used to exit `for`, `while`, or `do...while` loops prematurely.
*   **`if` / `else` / `else if`**: Control flow statements for conditional execution.
*   **`this`**: Refers to the current contract instance itself.
*   **`super`**: Used in inheritance to call functions from a parent contract.
*   **`new`**: Used to create new instances of contracts.
*   **`override`**: Explicitly states that a function or modifier changes the behavior defined in a base contract.

### Impact of Misusing Reserved Keywords

Incorrect usage of reserved keywords directly leads to compilation errors in Solidity. The compiler is designed to enforce the language's syntax and semantics, and any attempt to use a reserved keyword as a custom identifier will be flagged as a `ParserError`. This mechanism prevents developers from creating ambiguous code that could lead to unexpected behavior or security vulnerabilities in smart contracts. Proper understanding and adherence to keyword usage rules are crucial for creating high-quality and secure Solidity contracts.

### Best Practices for Naming

To avoid conflicts and ensure valid code, developers should adhere to established naming conventions in Solidity. Variable names should not begin with a numeral (0-9). Solidity variable names are also case-sensitive, meaning `Name` and `name` are treated as distinct variables. Following these guidelines helps maintain code readability and prevents unintentional use of reserved keywords as identifiers.

Bibliography
Cheatsheet — Documentation Solidity 0.8.13 - Read the Docs. (2022). https://solidity-fr.readthedocs.io/fr/latest/cheatsheet.html

Keywords in Solidity - GeeksforGeeks. (2023). https://www.geeksforgeeks.org/keywords-in-solidity/

Solidity — Solidity 0.8.30 documentation. (2025). https://docs.soliditylang.org/

Solidity Basic Syntax - Tutorialspoint. (2020). https://www.tutorialspoint.com/solidity/solidity_basic_syntax.htm

Solidity Quick Guide - Tutorialspoint. (2020). https://www.tutorialspoint.com/solidity/solidity_quick_guide.htm

Solidity Variables - Tutorialspoint. (2020). https://www.tutorialspoint.com/solidity/solidity_variables.htm

The 31 Reserved Keywords in Solidity. (2022). https://koha.hashnode.dev/the-31-reserved-keywords-in-solidity

The 31 Reserved Keywords in Solidity - DEV Community. (2022). https://dev.to/koha/the-31-reserved-keywords-in-solidity-bda

Units and Globally Available Variables - Solidity Documentation. (2025). https://docs.soliditylang.org/en/latest/units-and-global-variables.html



Generated by Liner
https://getliner.com/search/s/5926611/t/85976130