JavaScript Reserved Keywords

Wed Jun 25 2025

### Introduction to JavaScript Reserved Keywords

JavaScript reserved words, also known as reserved identifiers, are terms that hold special meaning within the language's syntax and thus cannot be employed as identifiers for elements such as variables, functions, or labels. These words are predefined and serve the built-in functionality of the programming language. The lexical structure of JavaScript, which defines the rules for combining characters into tokens, dictates that keywords are the smallest individual units of a program and are essential for the interpreter to understand the code. Using reserved words for identifiers would create conflicts and could lead to incorrect program output or errors.

### Categories of JavaScript Reserved Keywords

JavaScript's reserved keywords can be broadly categorized based on their current usage, future reservation, and historical context within different ECMAScript specifications.

**Standard Keywords**: These are words currently active and fundamental to JavaScript's syntax and operations. Examples include `break`, `case`, `catch`, `class`, `const`, `continue`, `debugger`, `default`, `delete`, `do`, `else`, `export`, `extends`, `finally`, `for`, `function`, `if`, `import`, `in`, `instanceof`, `new`, `return`, `super`, `switch`, `this`, `throw`, `try`, `typeof`, `var`, `void`, `while`, and `with`. The `const` keyword, for instance, denotes that a variable is a constant.

**Future Reserved Words**: These words are not presently used as keywords but are reserved for potential future use in JavaScript. This reservation strategy prevents naming conflicts with upcoming language features. Common examples of future reserved words include `enum`, `await`, `implements`, `interface`, `package`, `private`, `protected`, and `public`. Some of these are conditionally reserved; for example, `await` is reserved only within async function bodies or module code. Similarly, `implements`, `interface`, `package`, `private`, `protected`, and `public` are reserved only in strict mode.

**ES5 and ES6 Additions**: ECMAScript 5 and 6 introduced new keywords such as `class`, `const`, `export`, `extends`, `import`, `let`, `super`, `await`, and `enum`. Words like `let` and `yield` that started as special words in ES6 may still work as identifiers in non-strict mode due to backward compatibility requirements, but they will throw errors in strict mode. The `let` keyword declares variables limited to a block statement's scope.

**Removed Reserved Words**: Some words like `abstract`, `boolean`, `byte`, `char`, `double`, `final`, `float`, `goto`, `int`, `long`, `native`, `short`, `synchronized`, `throws`, `transient`, and `volatile` have been removed from the ECMAScript 5/6 standard. Although removed, it is still advised to avoid using them as variables because ECMAScript 5/6 might not have full browser support.

### Usage Restrictions of Reserved Keywords

Reserved words cannot be used as identifiers for variables, functions, classes, or labels in JavaScript. This restriction applies universally in JavaScript source text for standard keywords. For instance, declaring a variable with `const` or a function with `function` uses these keywords for their intended purpose, but attempting to name a variable `var` or `function` would lead to an error.

**Case Sensitivity**: JavaScript is a case-sensitive language, meaning `myVar`, `MyVar`, and `MYVAR` are treated as distinct entities. This case sensitivity also applies to reserved words; however, reserved words are typically written in lowercase, and attempting to use a case-variant of a reserved word as an identifier would still violate syntax rules if the base word is reserved.

**Strict Mode**: In strict mode, additional identifiers are reserved to enforce cleaner code and prevent common errors. Words like `implements`, `interface`, `package`, `private`, `protected`, `public`, and `static` are reserved only in strict mode. `enum` is reserved in both strict and sloppy modes. Strict mode also restricts `eval` and `arguments` from being declared as identifiers.

**Module Code and Async Functions**: Some words like `await` are only reserved when found in module code or the bodies of `async` functions. This contextual reservation ensures that new language features can be introduced without breaking existing code in other contexts.

**Backward Compatibility**: For backward compatibility, some keywords like `let` and `yield`, introduced in later ECMAScript versions, might not cause errors in older JavaScript environments or non-strict mode. However, it is strongly recommended to avoid using them as identifiers to ensure modern code adheres to best practices and avoids potential future conflicts.

### Impact of Using Reserved Keywords as Identifiers

Using reserved keywords as identifiers in JavaScript directly violates the language's syntax rules, resulting in a "SyntaxError: Unexpected reserved word" or similar "reserved identifier" error. When such an error occurs, the JavaScript code will not execute. This is because the JavaScript engine expects these words to perform their predefined functions and cannot interpret them as user-defined names.

The error indicates that a reserved word is used incorrectly in a context where an identifier is expected, such as a variable name, function name, or class name. This makes the code invalid and prevents parsing. These errors are crucial as they prevent the application from running and commonly stem from using keywords in places like variable names, function names, or improper positioning within the code.

### Examples of Errors with Reserved Keywords

Attempting to use reserved keywords as identifiers will lead to syntax errors. Below are specific examples illustrating these issues and their resolutions:

**Using Reserved Words as Variable Names**:
If a reserved word like `let` is used as a variable name, it will trigger an error.
```javascript
// Error Example
const let = 1; // SyntaxError: 'let' is a reserved identifier

// Resolution
const myValue = 1; // Use a non-reserved identifier
```

**Using Reserved Words as Function Names**:
Defining a function with a reserved keyword such as `delete` will also result in an "Unexpected reserved word" error.
```javascript
// Error Example
function delete() { // SyntaxError: Unexpected reserved word
  console.log("Delete function");
}

// Resolution
function removeData() { // Choose a different function name
  console.log("Remove function");
}
```

**Using Reserved Words in Class Declarations**:
Similarly, using a reserved word as a class name, like `class` itself, is not permitted and causes a syntax error.
```javascript
// Error Example
class class { // SyntaxError: 'class' is a reserved identifier (in older browsers)
  constructor(name) {
    this.name = name;
  }
}

// Resolution
class MyClass { // Ensure class declarations are correctly formatted
  constructor(name) {
    this.name = name;
  }
}
let obj = new MyClass("Example");
console.log(obj.name);
```

These errors highlight the importance of adhering to JavaScript's syntax rules by avoiding the use of reserved words in identifier contexts.

### Other Reserved Names and Avoidances

Beyond the explicitly listed reserved keywords, JavaScript developers should also avoid using certain other names as identifiers to prevent conflicts and ensure code integrity.

**JavaScript Built-in Objects, Properties, and Methods**: It is advisable to avoid using the names of JavaScript's built-in objects, their properties, and methods as identifiers. Examples of built-in objects include `Array`, `Boolean`, `Date`, `Function`, `Math`, `Number`, `Object`, `String`, and `Promise`. Built-in properties like `length` or `prototype` and methods such as `toString`, `shift`, `indexOf`, and `split` should also be avoided as variable or function names.

**HTML and Window Objects and Properties**: JavaScript is frequently used in web environments alongside HTML, and as such, developers should avoid using names of HTML and Window objects and properties as identifiers. This includes names like `alert`, `document`, `window`, `location`, `navigator`, `clientInformation`, `decodeURIComponent`, `encodeURIComponent`, and `offscreenBuffering`.

**HTML Event Handlers**: All HTML event handler names, such as `onclick`, `onmouseover`, `onload`, and `onsubmit`, should also be avoided as identifiers to prevent conflicts with browser-defined functionality.

**Java Reserved Words**: Given that JavaScript is often used in conjunction with Java, it is recommended to avoid using certain Java objects and properties as JavaScript identifiers to prevent potential issues in integrated environments.

Adhering to these guidelines helps maintain code clarity, prevent ambiguity, and ensures proper execution across various JavaScript environments.

Bibliography
Can I use reserved word as parameter of a function in javascript? (2017). https://stackoverflow.com/questions/44426734/can-i-use-reserved-word-as-parameter-of-a-function-in-javascript

ES6 & JavaScript Reserved Words. Tokens | by Claire Nguyen. (2019). https://medium.com/@clairenguyen/js-reserved-words-f324beef93fa

How do I use a Javascript keyword as a variable name? (2016). https://stackoverflow.com/questions/38645956/how-do-i-use-a-javascript-keyword-as-a-variable-name

JavaScript Keywords and Identifiers - Programiz. (2000). https://www.programiz.com/javascript/keywords-identifiers

JavaScript Reserved Keywords - Tutorialspoint. (n.d.). https://www.tutorialspoint.com/javascript/javascript_reserved_keywords.htm

JavaScript Reserved Words - GeeksforGeeks. (2024). https://www.geeksforgeeks.org/javascript/javascript-reserved-words/

JavaScript: Reserved Words - TechOnTheNet. (n.d.). https://www.techonthenet.com/js/reserved_words.php

JavaScript Reserved Words - W3Schools. (n.d.). https://www.w3schools.com/js/js_reserved.asp

JavaScript Reserved Words - W3Schools.am. (2020). https://w3schools.am/js/js_reserved.html

JavaScript Reserved Words.md - GitHub. (n.d.). https://github.com/AnanthaRajuC/Lists-of-Reserved-Words-of-various-programming-languages/blob/master/language-files/JavaScript%20Reserved%20Words.md

JavaScript SyntaxError – Unexpected reserved word - GeeksforGeeks. (2024). https://www.geeksforgeeks.org/javascript/javascript-syntaxerror-unexpected-reserved-word-1/

Lexical grammar - JavaScript - MDN Web Docs. (2025). https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar

Lexical Structure in JavaScript - Ajay Dhangar. (2024). https://ajaydhangar49.medium.com/lexical-structure-in-javascript-3a7828262220

List of keywords and reserved words in JavaScript - Flavio Copes. (2020). https://flaviocopes.com/javascript-reserved-words/

Reserved keywords in JavaScript - Mathias Bynens. (2013). https://mathiasbynens.be/notes/reserved-keywords

SyntaxError: “x” is a reserved identifier - JavaScript - MDN Web Docs. (2023). https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Reserved_identifier

Using reserved keyword as Identifiers - The freeCodeCamp Forum. (2020). https://forum.freecodecamp.org/t/using-reserved-keyword-as-identifiers/417534

What are JavaScript Reserved Words and Keywords? Edureka. (2025). https://www.edureka.co/blog/javascript-reserved-words/



Generated by Liner
https://getliner.com/search/s/5926611/t/85976152