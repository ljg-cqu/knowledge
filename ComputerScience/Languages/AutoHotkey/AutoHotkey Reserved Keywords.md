AutoHotkey Reserved Keywords

Wed Jun 25 2025

### Overview of AutoHotkey Reserved Keywords

AutoHotkey utilizes reserved keywords to define specific functionalities, operators, and control flow, which prevents their use as ordinary identifiers like variable names, function names, or class names. These reservations are crucial for maintaining the language's syntax and preventing unexpected behavior or errors in scripts. The specific set of reserved words varies slightly between AutoHotkey versions, with v2 introducing changes from v1.1 regarding certain keywords and their behaviors.

### General Reserved Keywords

A core set of words in AutoHotkey are consistently reserved for specific purposes, such as operators or boolean constants. These include `as`, `and`, `contains`, `false`, `in`, `is`, `IsSet`, `not`, `or`, `super`, `true`, and `unset`. These words cannot be used as variable names when written literally in an expression. For instance, `true` and `false` are built-in variables that contain `1` and `0` respectively, and their use makes scripts more readable for boolean values. Similarly, `not` acts as a logical-NOT operator, producing `1` for true and `0` for false. The `new` keyword is reserved for creating new objects derived from another object or class. The `unset` keyword, while reserved, can be used to explicitly unset certain elements, particularly function parameters, highlighting its specific functional reservation.

### Control Flow and Declaration Keywords

Beyond general operators, AutoHotkey also reserves words associated with control flow statements and declarations. This reservation primarily serves to detect mistakes and ensure proper script execution. These keywords include `Break`, `Catch`, `Continue`, `Else`, `Finally`, `For`, `Global`, `Goto`, `If`, `Local`, `Loop`, `Return`, `Static`, `Throw`, `Try`, `Until`, and `While`. Using these words as variable names or other identifiers will typically result in errors. For example, `break` has a special meaning to the parser, and its reservation helps detect errors where it might be mistakenly used as a variable name. The `if` statement, although appearing similar to an expression, is not, and its keyword `if` is reserved. These keywords define fundamental programming constructs and their reserved status prevents redefinition that could corrupt script logic.

### Nuances of the "Class" Keyword

The word "class" presents a unique and sometimes confusing case within AutoHotkey's reserved keywords. While `class` functions as both a built-in type and a reserved word, its restrictions are context-dependent. In AutoHotkey v2, `class` is not strictly reserved in the sense that it can be used as a variable name in certain contexts, such as a local variable name within a function. However, if `class` appears as a standalone instruction inside a function, it generates an error rather than being interpreted as a call to `Class()`. This behavior distinguishes it from keywords that are completely forbidden as identifiers. The documentation notes that `ClassOverwrite` has been removed in v2, meaning top-level classes can no longer be overwritten by assignment, though they can be shadowed by local variables. This design choice allows for flexibility while preventing accidental redefinition of a built-in class name, making it less likely that adding new built-in classes will break existing scripts.

### Restrictions and Usage Examples

The primary restriction for reserved keywords is their prohibition as variable names, function names, and class names in most contexts. For example, words like `and`, `contains`, `in`, `is`, `new`, `not`, and `or` are reserved for use as operators and cannot be directly used as variable names in expressions. Functions, classes, and window groups are subject to the same naming restrictions as variables. If a reserved word is used improperly, the AutoHotkey interpreter will typically throw an error indicating that the reserved word must not be used as a variable name.

For instance, trying to assign a value to `true` (e.g., `true := 5`) would lead to an error because `true` is a reserved constant. Similarly, attempting to define a function named `Loop` (e.g., `Loop() { ... }`) would be invalid as `Loop` is a control flow keyword.

Despite these restrictions, some reserved words can be utilized in specific, intended ways. For example, `new` is explicitly used for object creation (e.g., `x := new y`). The keyword `break` is correctly used within loops to exit them prematurely. In some cases, reserved words might be allowed as property names or window group names, particularly when preceded by a dot, as the interpreter recognizes the context. This implies that the parser evaluates the context of the word before enforcing the strict reserved keyword rule.

### Summary of AutoHotkey Reserved Keywords and Their Usage

The following table summarizes key AutoHotkey reserved keywords and their general usage or restrictions:

| Keyword Category       | Examples                                           | Usage/Restriction                                                                                                                                                                                                                                                                                               |
| :--------------------- | :------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **General Keywords**   | `as`, `and`, `contains`, `false`, `in`, `is`, `IsSet`, `not`, `or`, `super`, `true`, `unset` | Reserved for future use or specific purposes like operators and boolean constants; cannot be used as variable names when written literally in an expression. `true` and `false` are `1` and `0` respectively. `unset` is used for unsetting variables. |
| **Control Flow/Declaration** | `Break`, `Catch`, `Continue`, `Else`, `Finally`, `For`, `Global`, `Goto`, `If`, `Local`, `Loop`, `Return`, `Static`, `Throw`, `Try`, `Until`, `While` | Reserved to detect programming mistakes; cannot be used as variable, function, or class names. Using them as identifiers will result in errors.                                                                                                           |
| **Special Case: "Class"** | `class`                                     | Functions as both a built-in type/global variable and a reserved word depending on context. Can be used as a local variable, but a standalone `class` instruction within a function generates an error.                                                                 |
| **Operator Keywords**  | `new`, `not`, `and`, `or`             | Used for specific operations (e.g., `new` for object creation). `not`, `and`, `or` are logical operators.                                                                                                                                                   |

The comprehensive understanding of these reserved keywords and their specific contextual behaviors is essential for writing robust and error-free AutoHotkey scripts.

Bibliography
Changes from v1.1 to v2.0 | AutoHotkey v2. (n.d.). https://www.autohotkey.com/docs/v2/v2-changes.htm

Concepts and Conventions | AutoHotkey v2. (n.d.). https://www.autohotkey.com/docs/v2/Concepts.htm

Continuation section & reserved words error priority - AutoHotkey. (2018). https://www.autohotkey.com/boards/viewtopic.php?t=46902

[PDF] AutoHotkey Help - Documentation & Help. (n.d.). https://documentation.help/AutoHotkey-en/documentation.pdf

Reserved keywords vs class - AutoHotkey Community. (2021). https://www.autohotkey.com/boards/viewtopic.php?t=94335

The following reserved word must not be used as a variable name. (2021). https://www.autohotkey.com/boards/viewtopic.php?style=19&t=94660

The following reserved word must not be used as variable name. (2016). https://www.autohotkey.com/boards/viewtopic.php?t=24035

[v2.0-beta.7] Reserved words as properties. No error ... - AutoHotkey. (2022). https://www.autohotkey.com/boards/viewtopic.php?t=106852

Variables and Expressions - Auto Hotkey Documentation. (2004). https://documentation.help/AHK_H-2.0/Variables.htm

Variables and Expressions - Definition & Usage | AutoHotkey v1. (2023). https://www.autohotkey.com/docs/v1/Variables.htm



Generated by Liner
https://getliner.com/search/s/5926611/t/85976354