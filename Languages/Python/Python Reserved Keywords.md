Python Reserved Keywords

Wed Jun 25 2025

### Introduction to Python Reserved Keywords

In Python, **reserved keywords** are words that possess special meanings and are already predefined by the Python language. These keywords are integral to defining the structure and syntax of Python programs. Consequently, they cannot be utilized as variable names, function names, class names, or any other identifiers within a program, as doing so would result in syntax errors or unexpected behavior. Python has a fixed set of these keywords that the interpreter recognizes, and they cannot be redefined by the programmer. These special words instruct Python to perform specific actions, making them fundamental to the language's functionality.

### List of Python Reserved Keywords

Python provides 35 reserved keywords that are foundational to its syntax and functionality. The precise number of keywords may vary slightly with different Python versions, but Python 3.10.6 and later versions, including Python 3.11, contain 35 keywords. These keywords are case-sensitive, and all of them are entirely lowercase except for `False`, `None`, and `True`. The complete list of Python's reserved keywords includes: `False`, `None`, `True`, `and`, `as`, `assert`, `async`, `await`, `break`, `class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `nonlocal`, `not`, `or`, `pass`, `raise`, `return`, `try`, `while`, `with`, and `yield`.

### Purpose and Usage of Each Reserved Keyword

Each Python keyword serves a distinct purpose, contributing to the language's expressiveness and control structures.

#### Boolean and Null Constants
*   **`False`**: This keyword represents the boolean value `False`, indicating an untrue or "no" condition. It is one of the two Boolean constants in Python, equivalent to the integer `0`. For instance, a statement like `print(False == 0)` would output `True`.
*   **`None`**: `None` is a special constant that signifies the absence of a value or a null value. It has its own data type, `NoneType`, and is not equivalent to `False`, `0`, or an empty string. For example, `print(None == False)` will return `False`. All variables assigned `None` are equal to each other, such as `x = None; y = None; print(x is y)` yielding `True`.
*   **`True`**: This keyword represents the boolean value `True`, indicating a true condition. It is the other Boolean constant in Python and is equivalent to the integer `1`. An example showing its usage is `print(True and True)`, which outputs `True`.

#### Logical Operators
*   **`and`**: The `and` keyword is a logical operator used to combine two conditions, returning `True` only if both conditions are `True`. An example is `if a > 0 and b > 0: print("Both are positive")`.
*   **`or`**: The `or` keyword is a logical operator that returns `True` if at least one of the conditions it combines is `True`. For example, `if temperature > 30 or humidity > 80: print("It's extreme weather")`.
*   **`not`**: This is a logical operator that inverts the truth value of a condition. If a condition is `True`, `not` makes it `False`, and vice-versa. An example is `if not is_admin: print("Access denied")`.

#### Conditional Statements
*   **`if`**: The `if` keyword initiates a conditional statement, executing a block of code only if a specified Boolean condition is `True`. An example includes `if x > 10: print("x is greater than 10")`.
*   **`elif`**: Short for "else if," `elif` is used in conditional statements to check additional conditions sequentially if the preceding `if` or `elif` conditions were `False`. For instance, `if x > 0: print("Positive") elif x == 0: print("Zero")`.
*   **`else`**: The `else` keyword defines a block of code that executes if none of the preceding `if` or `elif` conditions are met. An example would be `if age >= 18: print("Adult") else: print("Minor")`.

#### Looping Statements
*   **`for`**: The `for` keyword is used to create loops for iterating over a sequence, such as a list, tuple, string, or range. It assigns each item from the sequence to a variable, and the code within the loop executes once for each item. An example is `for item in my_list: print(item)`.
*   **`while`**: The `while` keyword is used to create a loop that repeatedly executes a block of code as long as a given condition remains `True`. The condition is evaluated before each iteration, and the loop continues until the condition becomes `False`. An example is `count = 0; while count < 5: print(count); count += 1`.
*   **`break`**: The `break` keyword is used to exit the innermost loop completely, transferring the control of execution to the statement immediately following the loop. For instance, `for i in range(10): if i == 5: break` would stop the loop when `i` reaches 5.
*   **`continue`**: This keyword alters the flow of a loop by skipping the rest of the current iteration and proceeding directly to the next iteration. An example is `for i in range(5): if i % 2 == 0: continue; print(i)` which prints only odd numbers.

#### Function and Class Definition
*   **`def`**: The `def` keyword is used to define functions or methods in Python. A function defined with `def` is a block of code that performs specific tasks and can be reused. An example is `def greet(name): print(f"Hello, {name}")`.
*   **`class`**: The `class` keyword is used to define a new class, which serves as a blueprint for creating objects in object-oriented programming. It encapsulates data members and functions, providing state and behavior for objects. An example is `class Dog: def __init__(self, name): self.name = name`.
*   **`return`**: The `return` keyword is used inside a function to exit it and optionally return a value to the caller. If no value is explicitly returned, the function implicitly returns `None`. For example, `def add(a, b): return a + b`.
*   **`yield`**: The `yield` keyword is used in generator functions to produce a sequence of values lazily, one at a time, without storing the entire sequence in memory. Unlike `return`, `yield` allows a function to "pause" its execution and "resume" from where it left off, returning a value each time it's called. An example is `def countdown(n): while n > 0: yield n; n -= 1`.
*   **`lambda`**: The `lambda` keyword is used for creating anonymous functions, also known as lambda functions. These are single-line functions without a name, typically used for simple, one-line operations where a named function is unnecessary. An example is `add_one = lambda x: x + 1`.

#### Importing Mechanisms
*   **`import`**: The `import` keyword is used to bring external modules or packages into your Python program, making their contents (functions, classes, variables) available for use. For example, `import math` allows access to mathematical functions like `math.sqrt()`.
*   **`from`**: The `from` keyword is typically used with `import` to import specific attributes, functions, or classes from a module, rather than importing the entire module. This helps reduce namespace clutter and improves code readability. An example is `from math import pi, sqrt` to directly use `pi` and `sqrt`. It can also be used in generator functions (e.g., `yield from`) and exception handling (e.g., `raise ... from ...`).
*   **`as`**: The `as` keyword is used to create an alias or an alternative, often shorter, name for a module, exception, or context manager during `import` statements or in `try...except...as` blocks. This enhances code readability and can prevent naming conflicts. An example is `import numpy as np`.

#### Exception Handling
*   **`try`**: The `try` keyword defines a block of code that Python will attempt to execute, and which may raise an exception. If an error occurs within this block, Python jumps to the associated `except` block. An example is `try: result = 10 / 0`.
*   **`except`**: The `except` keyword defines a block of code to run if an error or exception is raised within the preceding `try` block. It allows for specific exception handling. For instance, `except ZeroDivisionError: print("Cannot divide by zero")`.
*   **`finally`**: The `finally` keyword is used in a `try` statement to define a block of code that will always execute, regardless of whether an exception was raised or handled. This is typically used for cleanup actions, such as closing files or network connections. An example is `finally: print("Execution finished")`.
*   **`raise`**: The `raise` keyword is used to explicitly raise exceptions or errors in Python programs. It allows you to create and raise custom exceptions or propagate built-in exceptions, interrupting the normal flow of the program to handle exceptional situations. For example, `raise ValueError("Invalid input")`.
*   **`assert`**: The `assert` keyword is primarily used for debugging and testing purposes. It checks if a given condition is `True`, and if the condition evaluates to `False`, it raises an `AssertionError` with an optional error message. An example is `assert x < 10, "x is not less than 10"`.

#### Variable Scope
*   **`global`**: The `global` keyword is used within a function to declare that a variable refers to a global variable, allowing its modification from a non-global scope. Without `global`, assigning a new value to an existing global variable inside a function would create a local variable with the same name. An example is `count = 0; def increment(): global count; count += 1`.
*   **`nonlocal`**: The `nonlocal` keyword is used within nested functions to declare that a variable refers to a variable in an enclosing function's scope (but not the global scope), allowing the inner function to modify it. This keyword is crucial when an inner function needs to change the state of a variable defined in its immediate outer function. For instance, `def outer(): x = 5; def inner(): nonlocal x; x += 1`.

#### Resource Management
*   **`with`**: The `with` keyword is used in a context manager statement to simplify the management of resources, such as files or network connections. It ensures that resources are properly acquired and released, even if an exception occurs, by guaranteeing the execution of setup and teardown actions. A common use case is opening files, like `with open('file.txt', 'w') as f: f.write('Hello')`.

#### Object Manipulation and Testing
*   **`del`**: The `del` keyword is used to delete objects, variables, elements from lists, or entries from dictionaries in Python. When used with variables, it releases the memory occupied by the variable, making it inaccessible. For example, `my_list = [1, 2, 3]; del my_list[0]` would remove the first element.
*   **`in`**: The `in` keyword serves two primary purposes: it acts as a membership operator to check if a value is present within a sequence (like a list, tuple, or string), and it is used for iteration in `for` loops. For example, `if 'apple' in my_fruits: print("Found")` or `for char in 'Python': print(char)`.
*   **`is`**: The `is` keyword is an identity operator used to test if two variables refer to the exact same object in memory, meaning they share the same memory location. It returns `True` if both objects are identical; otherwise, it returns `False`. For instance, `a = []; b = []; print(a is b)` would yield `False` because they are distinct objects in memory, even if their content is the same.

#### Asynchronous Programming
*   **`async`**: The `async` keyword is used to define asynchronous functions or methods, known as coroutines. These functions allow for concurrent code execution without blocking the main program flow, enabling efficient handling of I/O-bound operations. An example is `async def fetch_data(): await some_io_operation()`.
*   **`await`**: The `await` keyword is used inside an `async` function to pause its execution until a specific asynchronous operation (an awaitable object like a coroutine or a Future) completes. This suspension allows other coroutines to run concurrently, improving application responsiveness. An example is `await asyncio.sleep(1)` within an `async` function.

### Accessing Python Keywords

Python offers convenient ways to access the list of its reserved keywords directly within the interpreter. One method is to use the built-in `help()` function with the argument `"keywords"`. Executing `help("keywords")` in the Python terminal will display the comprehensive list of keywords available. Additionally, this command provides guidance on how to get more specific help for any individual keyword by entering its name into `help()`. For example, `help("False")` provides detailed documentation on the `False` keyword. To exit this help view, one can simply press the `q` character.

Another method to retrieve the list of keywords is by importing the `keyword` module, which is part of Python's standard library, and then accessing its `kwlist` attribute. The command `import keyword; print(keyword.kwlist)` will return the list of all reserved keywords as a list of strings. This module also includes a function `keyword.iskeyword()` which allows checking if a specific string is a reserved keyword, returning `True` or `False`.

### Common Errors and Best Practices

A common error in Python programming arises from attempting to use reserved keywords as variable names or identifiers. Because these words have special meanings for the Python interpreter, using them for other purposes will lead to `SyntaxError` or `TypeError`. For example, trying to assign a value to `for` (e.g., `for = 5`) or define a function named `while` (e.g., `def while(): pass`) will result in a `SyntaxError`. This confusion arises because the keywords are part of Python's syntax, and the interpreter expects them to perform their predefined roles. Similarly, using reserved keywords as method names within a class or as dictionary keys can also cause `SyntaxError`.

To avoid these errors, it is crucial to select meaningful and descriptive names for variables, functions, and other identifiers that do not conflict with Python's reserved keywords. While Python allows shadowing built-in functions (like `list`), it is generally advisable to avoid doing so, as it can make code less readable and potentially lead to unexpected behavior by making the original built-in inaccessible in that scope. In situations where variable naming could be ambiguous, referring to the list of keywords using `help("keywords")` or `keyword.kwlist` can help prevent common pitfalls. Adhering to these best practices ensures smooth execution of code and improves its readability and maintainability for other programmers.

Bibliography
5 Ways to Use Pass Keyword in Python Effectively - AceNet Hub. (2025). https://www4.acenet.edu/pass-keyword-in-python

8. Errors and Exceptions — Python 3.13.5 documentation. (n.d.). https://docs.python.org/3/tutorial/errors.html

as | Python Keywords – Real Python. (n.d.). https://realpython.com/ref/keywords/as/

as Keyword - Python - GeeksforGeeks. (2025). https://www.geeksforgeeks.org/python-as-keyword/

Assert in Python: What is it and How to use it - BrowserStack. (n.d.). https://www.browserstack.com/guide/assert-in-python

Async IO in Python: A Complete Walkthrough. (n.d.). https://realpython.com/async-io-python/

asyncio — Asynchronous I/O — Python 3.13.5 documentation. (n.d.). https://docs.python.org/3/library/asyncio.html

Asyncio in Python: A Comprehensive Guide with Examples. - Medium. (2024). https://medium.com/@obaff/asyncio-in-python-a-comprehensive-guide-with-examples-3a3f854017f9

await | Python Keywords. (n.d.). https://realpython.com/ref/keywords/await/

Can I see some good example of “is” keyword in Python? How it’s ... (2018). https://www.quora.com/Can-I-see-some-good-example-of-is-keyword-in-Python-How-it-s-useful

Can someone explain to me the “return” function? : r/learnpython. (2022). https://www.reddit.com/r/learnpython/comments/t7dx6b/can_someone_explain_to_me_the_return_function/

Context Managers and Python’s with Statement - Real Python. (n.d.). https://realpython.com/python-with-statement/

continue | Python Keywords. (n.d.). https://realpython.com/ref/keywords/continue/

del | Python Keywords. (n.d.). https://realpython.com/ref/keywords/del/

else | Python Keywords. (n.d.). https://realpython.com/ref/keywords/else/

False | Python Keywords. (n.d.). https://realpython.com/ref/keywords/false/

finally | Python Keywords. (n.d.). https://realpython.com/ref/keywords/finally/

from | Python Keywords – Real Python. (2012). https://realpython.com/ref/keywords/from/

global | Python Keywords. (n.d.). https://realpython.com/ref/keywords/global/

Global keyword in Python - GeeksforGeeks. (2025). https://www.geeksforgeeks.org/python/global-keyword-in-python/

How does the “in” keyword work? : r/learnpython - Reddit. (2021). https://www.reddit.com/r/learnpython/comments/moyhyh/how_does_the_in_keyword_work/

How to Use Generators and yield in Python. (n.d.). https://realpython.com/introduction-to-python-generators/

How to Use IF Statements in Python (if, else, elif, and more). (2022). https://www.dataquest.io/blog/tutorial-using-if-statements-in-python/

How to use “pass” statement? - python - Stack Overflow. (2012). https://stackoverflow.com/questions/13886168/how-to-use-pass-statement

if | Python Keywords. (n.d.). https://realpython.com/ref/keywords/if/

Import module in Python - GeeksforGeeks. (2025). https://www.geeksforgeeks.org/python/import-module-python/

Importing a package with a keyword in path - python - Stack Overflow. (2021). https://stackoverflow.com/questions/65775394/importing-a-package-with-a-keyword-in-path

Learn About the Nonlocal Keyword in Python Programming. (2024). https://dev.to/devstoriesplayground/learn-about-the-nonlocal-keyword-in-python-programming-4h24

List of Reserved Keywords in Python - Scientech Easy. (2025). https://www.scientecheasy.com/2022/09/reserved-keywords-in-python.html/

nonlocal | Python Keywords. (n.d.). https://realpython.com/ref/keywords/nonlocal/

not | Python Keywords. (n.d.). https://realpython.com/ref/keywords/not/

not Operator in Python - GeeksforGeeks. (2025). https://www.geeksforgeeks.org/python/python-not-keyword/

print first and last name with def keyword in python - Stack Overflow. (2020). https://stackoverflow.com/questions/61691571/print-first-and-last-name-with-def-keyword-in-python

python 3.x - Examples of While loops - Stack Overflow. (2023). https://stackoverflow.com/questions/75951517/examples-of-while-loops

Python And Keyword - GeeksforGeeks. (2025). https://www.geeksforgeeks.org/python/python-and-keyword/

Python and Keyword - W3Schools. (n.d.). https://www.w3schools.com/python/ref_keyword_and.asp

Python Assert Statement - Programiz. (n.d.). https://www.programiz.com/python-programming/assert-statement

Python break and continue (With Examples) - Programiz. (n.d.). https://www.programiz.com/python-programming/break-continue

Python break Keyword - W3Schools. (n.d.). https://www.w3schools.com/python/ref_keyword_break.asp

Python class Keyword - W3Schools. (n.d.). https://www.w3schools.com/python/ref_keyword_class.asp

Python Class: Syntax and Examples [Python Tutorial] - Mimo. (n.d.). https://mimo.org/glossary/python/class

Python Conditions and If statements - W3Schools. (n.d.). https://www.w3schools.com/python/python_conditions.asp

Python continue Keyword - W3Schools. (n.d.). https://www.w3schools.com/python/ref_keyword_continue.asp

Python Continue Statement - Tutorialspoint. (n.d.). https://www.tutorialspoint.com/python/python_continue_statement.htm

Python def Keyword - GeeksforGeeks. (2024). https://www.geeksforgeeks.org/python/python-def-keyword/

Python del Keyword - W3Schools. (n.d.). https://www.w3schools.com/python/ref_keyword_del.asp

Python else Keyword - W3Schools. (n.d.). https://www.w3schools.com/python/ref_keyword_else.asp

Python except Keyword - W3Schools. (n.d.). https://www.w3schools.com/python/ref_keyword_except.asp

Python Exception Handling - GeeksforGeeks. (2025). https://www.geeksforgeeks.org/python-exception-handling/

Python Exception Handling (With Examples) - Programiz. (n.d.). https://www.programiz.com/python-programming/exception-handling

Python False Keyword - GeeksforGeeks. (2025). https://www.geeksforgeeks.org/python/python-false-keyword/

Python False Keyword - Tutorialspoint. (n.d.). https://www.tutorialspoint.com/python/python_false_keyword.htm

Python finally block - Studytonight. (n.d.). https://www.studytonight.com/python/finally-block-in-python

Python finally Keyword - W3Schools. (n.d.). https://www.w3schools.com/python/ref_keyword_finally.asp

Python for Keyword - W3Schools. (n.d.). https://www.w3schools.com/python/ref_keyword_for.asp

Python Functions – How to Define and Call a Function. (2022). https://www.freecodecamp.org/news/python-functions-define-and-call-a-function/

Python global Keyword - W3Schools. (n.d.). https://www.w3schools.com/python/ref_keyword_global.asp

Python Global Variables | Definition, Scope and Examples. (2025). https://www.simplilearn.com/tutorials/python-tutorial/global-variable-in-python

Python If Elif - W3Schools. (n.d.). https://www.w3schools.com/python/gloss_python_elif.asp

Python if, if...else Statement (With Examples) - Programiz. (n.d.). https://www.programiz.com/python-programming/if-elif-else

Python Import: Mastering The Advanced Features - Mend.io. (2023). https://www.mend.io/blog/python-import-mastering-the-advanced-features/

Python in Keyword - GeeksforGeeks. (2025). https://www.geeksforgeeks.org/python/python-in-keyword/

Python in Keyword - W3Schools. (n.d.). https://www.w3schools.com/python/ref_keyword_in.asp

Python Keywords - CodingNomads. (2024). https://codingnomads.com/python-keywords

Python lambda Keyword - W3Schools. (n.d.). https://www.w3schools.com/python/ref_keyword_lambda.asp

Python nonlocal Keyword - GeeksforGeeks. (2025). https://www.geeksforgeeks.org/python/python-nonlocal-keyword/

Python nonlocal Keyword - W3Schools. (n.d.). https://www.w3schools.com/python/ref_keyword_nonlocal.asp

Python not Keyword - W3Schools. (n.d.). https://www.w3schools.com/python/ref_keyword_not.asp

Python Not Operator: Master Logical Negation | Learn Now! - Mimo. (n.d.). https://mimo.org/glossary/python/the-not-operator

Python pass Keyword - W3Schools. (2025). https://www.w3schools.com/python/ref_keyword_pass.asp

Python pass Statement - GeeksforGeeks. (2025). https://www.geeksforgeeks.org/python/python-pass-statement/

Python pass Statement (With Examples) - Programiz. (n.d.). https://www.programiz.com/python-programming/pass-statement

Python Raise Keyword - GeeksforGeeks. (2023). https://www.geeksforgeeks.org/python/python-raise-keyword/

Python raise Keyword - W3Schools. (2025). https://www.w3schools.com/python/ref_keyword_raise.asp

Python Reserved Keywords: A Comprehensive Explanation - Medium. (2023). https://medium.com/@pydatageek/python-reserved-keywords-a-comprehensive-explanation-426f763adbea

Python return Keyword - W3Schools. (n.d.). https://www.w3schools.com/python/ref_keyword_return.asp

Python return statement | DigitalOcean. (2022). https://www.digitalocean.com/community/tutorials/python-return-statement

Python True Keyword - W3Schools. (n.d.). https://www.w3schools.com/python/ref_keyword_true.asp

Python Try Except - W3Schools. (n.d.). https://www.w3schools.com/python/python_try_except.asp

Python try Keyword - W3Schools. (n.d.). https://www.w3schools.com/python/ref_keyword_try.asp

Python Try-Finally Block - Tutorialspoint. (n.d.). https://www.tutorialspoint.com/python/python_tryfinally_block.htm

Python while Loops: Repeating Tasks Conditionally. (2025). https://realpython.com/python-while-loop/

Python yield Keyword - W3Schools. (2025). https://www.w3schools.com/python/ref_keyword_yield.asp

Python yield Keyword: What Is It and How to Use It? - DataCamp. (2024). https://www.datacamp.com/tutorial/yield-python-keyword

Pythonic ways to use “else” in a for loop [duplicate] - Stack Overflow. (2009). https://stackoverflow.com/questions/685758/pythonic-ways-to-use-else-in-a-for-loop

Python’s del: Remove References From Scopes and Containers. (n.d.). https://realpython.com/python-del-statement/

Python’s “in” and “not in” Operators: Check for Membership. (2025). https://realpython.com/python-in-operator/

Reserved Keywords in Python - Tutorialspoint. (2017). https://www.tutorialspoint.com/What-are-Reserved-Keywords-in-Python

Reserved Keywords (Video) - Real Python. (2019). https://realpython.com/lessons/reserved-keywords/

Reserved words in Python - Python Morsels. (2023). https://www.pythonmorsels.com/reserved-words-in-python/

Simplest async/await example possible in Python - Stack Overflow. (2018). https://stackoverflow.com/questions/50757497/simplest-async-await-example-possible-in-python

Still confused on what the “def” feature is on Python *Warning, I am a ... (2019). https://www.reddit.com/r/learnpython/comments/admojm/still_confused_on_what_the_def_feature_is_on/

try catch - How to work with try and except in python? - Stack Overflow. (n.d.). https://stackoverflow.com/questions/62062226/how-to-work-with-try-and-except-in-python

Try Statement in Python - Hyperskill. (2024). https://hyperskill.org/university/python/try-statement-in-python

try…except…finally in Python - GUVI. (n.d.). https://www.guvi.in/hub/python/try-except-finally-in-python/

Understanding Python’s Assert Keyword: Effective Debugging. (2024). https://www.upgrad.com/tutorials/software-engineering/python-tutorial/assert-keyword-in-python/

Understanding the the “del” keyword - Dataquest Community. (2020). https://community.dataquest.io/t/understanding-the-the-del-keyword/397346

Usage of `global`- yes or nogo? : r/Python - Reddit. (2021). https://www.reddit.com/r/Python/comments/qj692s/usage_of_global_yes_or_nogo/

Using the “or” operator to assign variables - Python - Reddit. (2022). https://www.reddit.com/r/Python/comments/v8ee4a/using_the_or_operator_to_assign_variables/

What Does the `yield` Keyword in Python Do? - Sentry. (2022). https://sentry.io/answers/python-yield-keyword/

What is `lambda` in Python code? How does it work with `key ... (2012). https://stackoverflow.com/questions/13669252/what-is-lambda-in-python-code-how-does-it-work-with-key-arguments-to-sorte

What is a pass in Python? Give example - Quora. (2023). https://www.quora.com/What-is-a-pass-in-Python-Give-example

what is “nonlocal” ? : r/learnpython - Reddit. (2022). https://www.reddit.com/r/learnpython/comments/x47ptf/what_is_nonlocal/

What is the difference between a class and a function? When to use ... (2023). https://www.reddit.com/r/learnpython/comments/14wv1h0/what_is_the_difference_between_a_class_and_a/

What is the import keyword in Python? - Quora. (2024). https://www.quora.com/What-is-the-import-keyword-in-Python

What is the None keyword in Python? - Educative.io. (n.d.). https://www.educative.io/answers/what-is-the-none-keyword-in-python

What is the purpose of Lambda expressions? - Python Help. (2021). https://discuss.python.org/t/what-is-the-purpose-of-lambda-expressions/12415

What is the use of logical NOT operator? - learnpython - Reddit. (2022). https://www.reddit.com/r/learnpython/comments/uxynbc/what_is_the_use_of_logical_not_operator/

What Is the With Statement in Python? | Built In. (n.d.). https://builtin.com/software-engineering-perspectives/what-is-with-statement-python

What’s a real world example for using “while” loops? - Codecademy. (n.d.). https://www.codecademy.com/forum_questions/5130254c3ecc9d8c45003f70

While Loop in Python 3 using lists and if-statement for begginer. (2019). https://stackoverflow.com/questions/55450907/while-loop-in-python-3-using-lists-and-if-statement-for-begginer

Why isn’t the “global” keyword needed to access a global variable? (2011). https://stackoverflow.com/questions/4693120/why-isnt-the-global-keyword-needed-to-access-a-global-variable



Generated by Liner
https://getliner.com/search/s/5926611/t/85976170