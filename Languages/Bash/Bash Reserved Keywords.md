Bash Reserved Keywords

Wed Jun 25 2025

### Definition of Bash Reserved Keywords

Bash reserved keywords, also known as reserved words, are terms that hold a specific meaning for the Bash shell. These words are integral to the shell's grammar and are primarily used to initiate or terminate compound commands. Unlike regular commands, keywords are recognized and processed by Bash at a very early stage of its parsing process. This early recognition allows Bash to implement sophisticated behaviors and control structures that would not be possible with standard built-in commands or external utilities. For instance, `if` is classified as a shell keyword. There are almost 60 built-in commands and over 20 reserved words in Bash.

### Distinctions Between Keywords and Built-in Commands

While both shell keywords and built-in commands are internal to Bash, there is a fundamental difference in how Bash processes them. A built-in command behaves much like an external command, in that it is executed with arguments after variable expansion, word splitting, and globbing have occurred. Examples of built-in commands include `cd` and `test` (represented by `[`). Built-in commands are contained within Bash itself, making them more efficient than external commands that require separate files.

In contrast, keywords are scanned and understood by Bash at a much earlier stage of parsing. This allows Bash to apply special handling to the content associated with these keywords, such as preventing word splitting or pathname expansion. For example, `[[` is a shell keyword, whereas `[` is a shell built-in command. The `[[` keyword is considered safer because it prevents word splitting of string variables that contain spaces, eliminating the need for double quoting in many cases, although double-quoting remains a good practice. Additionally, `[[` offers features like regular expression matching. The difference is evident when handling strings with spaces: using `[[ -n $string_with_spaces ]]` works correctly without quoting, while `[ -n $string_with_spaces ]` results in an error due to word splitting. Keywords do not function as standalone commands; instead, they serve as subunits of command constructs, signaling specific code blocks like loops or conditional statements.

### Comprehensive List of Bash Reserved Keywords

The complete set of reserved words in Bash includes terms critical for flow control and command structuring. According to authoritative sources like the GNU Bash Reference Manual, these include:
*   `!`
*   `case`
*   `coproc`
*   `do`
*   `done`
*   `elif`
*   `else`
*   `esac`
*   `fi`
*   `for`
*   `function`
*   `if`
*   `in`
*   `select`
*   `then`
*   `time`
*   `until`
*   `while`
*   `{`
*   `}`
*   `[[`
*   `]]`

Some of these words, such as `in` and `do`, are only recognized as reserved words under specific conditions, like when they appear as the third word in a `case` or `for` command. The `time` command is listed as a keyword in official Bash documentation, enabling the timing of shell built-ins, functions, and pipelines.

### Usage Examples of Bash Reserved Keywords in Shell Scripts

Bash reserved keywords are essential for constructing logical and controlled script execution flows. They enable decision-making, iteration, and structured command execution within shell scripts.

#### Conditional Statements (`if`, `then`, `elif`, `else`, `fi`, `[[`, `]]`)

Conditional statements allow scripts to execute different code blocks based on whether a certain criterion is met. The `if`, `then`, `elif`, `else`, and `fi` keywords are fundamental to this process.

An `if` statement can be used to check conditions sequentially. If a test condition evaluates to `True`, the corresponding code block is executed, and subsequent conditions are not evaluated. The `fi` keyword marks the end of an `if` construct, which is a shell compound command. A `True` return status is indicated by zero, while a non-zero status indicates `False`. It is mandatory to have whitespace before and after the square brackets that enclose the testing condition.

Here is an example demonstrating conditional logic for checking file or directory types:
```bash
if [[ $# -eq 1 ]]; then # Checks if exactly one argument is provided
  if [ -f "$1" ]; then # Checks if the first argument is a regular file
    echo "The argument is a file, displaying its contents ..."
    cat "$1" # Displays content if it's a file
  elif [ -d "$1" ]; then # Checks if the first argument is a directory
    echo "The argument is a directory, running ls -l ..."
    ls -l "$1" # Lists contents if it's a directory
  else
    echo "The argument ($1) is neither a file nor a directory."
  fi
else
  echo "The script should be run with an argument."
fi
```
This example shows a nested `if` structure, where an inner `if` statement is contained within an outer one. The double square brackets `[[` and `]]` provide enhanced safety by preventing word splitting of string variables, unlike single square brackets `[` and `]`.

For numerical comparisons, Bash supports various operators within `[[ ]]` or `[ ]`:
*   `-eq`: Checks if two integers are equal (equivalent to `==`).
*   `-ne`: Returns true if operands are not equal.
*   `-gt`: Checks if the left integer is greater than the right integer (equivalent to `>`).
*   `-ge`: Checks if the left integer is greater than or equal to the right integer (equivalent to `>=`).
*   `-lt`: Checks if the left integer is less than the right integer (equivalent to `<`).
*   `-le`: Checks if the left integer is less than or equal to the right integer (equivalent to `<=`).

An example of numerical comparison for age validation:
```bash
read -p "Enter your age: " age # Prompts user for age
if [[ $age -lt 18 && $age -ge 0 ]]; then # Checks if age is less than 18 AND non-negative
  echo "You are a minor!"
elif [[ $age -eq 18 ]]; then # Checks if age is exactly 18
  echo "Congratulations, you've just become major!"
elif [[ $age -gt 18 && $age -le 100 ]]; then # Checks if age is greater than 18 AND less than or equal to 100
  echo "You are a major!"
else
  echo "Invalid age!"
fi
```
This script incorporates logical operators like `&&` (AND) to combine multiple conditions.

For string comparisons, the single equal sign `=` is used with single square brackets `[ ]`, while the double equal sign `==` is used with double square brackets `[[ ]]`. The inequality operator is `!=`. To check if a string contains a substring, asterisks `*` can be used as wildcards, such as `*"substring"*`. To check if a string is empty or not, `-z` returns true if the string length is zero, and `-n` returns true if the string length is non-zero.

#### Looping Constructs (`for`, `while`, `until`, `do`, `done`)

Loops enable repetitive execution of commands.
The `while` loop checks a condition and continues looping as long as the condition remains true. It requires a counter statement to control execution.
```bash
i=1 # Initializes counter
while [[ $i -le 10 ]]; do # Loop continues as long as 'i' is less than or equal to 10
  echo "Number: $i"
  (( i += 1 )) # Increments 'i'
done
```
The `for` loop executes statements a specific number of times or iterates over a list of items.
```bash
for fruit in apple banana orange; do # Iterates over a list of fruits
  echo "Fruit: $fruit"
done
```

#### Case Statements (`case`, `esac`)

`case` statements are used for multi-way branching, comparing a value against a list of patterns and executing the corresponding code block upon the first match. The `esac` keyword terminates the `case` statement.
```bash
fruit="apple"
case "$fruit" in # Checks the value of 'fruit'
  apple)
    echo "This is a red fruit.";; # Code for 'apple'
  banana)
    echo "This is a yellow fruit.";; # Code for 'banana'
  orange)
    echo "This is an orange fruit.";; # Code for 'orange'
  *)
    echo "Unknown fruit.";; # Default case if no pattern matches
esac
```

#### Function Definition (`function`)

The `function` keyword is used to define shell functions, which are blocks of reusable code.
```bash
function greet { # Defines a function named 'greet'
  echo "Hello, $1!" # $1 refers to the first argument passed to the function
}
greet "Alice" # Calls the function
```

#### Command Grouping (`{`, `}`)

Braces `{` and `}` are used to group commands, allowing them to be treated as a single unit. This is particularly useful when combined with keywords like `time` to measure the execution duration of a block of commands.
```bash
time { # Measures the execution time of the enclosed commands
  ls -l # Lists files in long format
  sleep 1 # Pauses for 1 second
}
```

These examples illustrate how Bash reserved keywords are fundamental building blocks for creating robust and intelligent shell scripts, enabling control over program flow and handling various types of data.

Bibliography
Bash Reference Manual. (n.d.). https://www.gnu.org/s/bash/manual/bash.pdf

Bash reserved words vs. built-in commands, and formatting the ... (2011). https://superuser.com/questions/301090/bash-reserved-words-vs-built-in-commands-and-formatting-the-output-of-the-time

Bash Scripting Tutorial – Linux Shell Script and Command Line for ... (2023). https://www.freecodecamp.org/news/bash-scripting-tutorial-linux-shell-script-and-command-line-for-beginners/

Getting help on Bash’s reserved words - Unix & Linux Stack Exchange. (2019). https://unix.stackexchange.com/questions/511085/getting-help-on-bashs-reserved-words

GNU bash manual page. (n.d.). http://www.employees.org/univercd/Feb-1998/cc/td/doc/product/atm/l2020/l2020r21/clicard/npos/gnubash.htm

GNU Bash Reference Manual. (2022). https://www.gnu.org/software/bash/manual/bash.html

How to list all the shell keywords? - command line - Ask Ubuntu. (2014). https://askubuntu.com/questions/445753/how-to-list-all-the-shell-keywords

How To Use Bash If Statements (With Code Examples). (2023). https://zerotomastery.io/blog/bash-if-statements/

How to Write a Bash Script: A Simple Bash Scripting Tutorial. (2022). https://www.datacamp.com/tutorial/how-to-write-bash-script-tutorial

Internal Commands and Builtins - The Linux Documentation Project. (n.d.). https://tldp.org/LDP/abs/html/internal.html

Reserved Word Index - Bash Reference Manual. (n.d.). https://bash.cyberciti.biz/bash-reference-manual/Reserved-Word-Index.html

Reserved Words and Built-In Commands - Pro Bash Programming. (n.d.). https://www.oreilly.com/library/view/pro-bash-programming/9781484201213/9781484201220_Ch09.xhtml

Reserved Words (Bash Reference Manual) - GNU. (n.d.). https://www.gnu.org/software/bash/manual/html_node/Reserved-Words.html

What’s the difference between shell builtin and shell keyword? (2014). https://askubuntu.com/questions/445749/whats-the-difference-between-shell-builtin-and-shell-keyword



Generated by Liner
https://getliner.com/search/s/5926611/t/85976332