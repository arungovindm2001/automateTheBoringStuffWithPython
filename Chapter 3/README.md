## 1. Why are functions advantageous to have in your programs?

Since variables exist in their local scopes, this is helpful when it comes to debugging your code. It is a great tool to help you organize your code.
If you need to execute a large amount of code many times, putting the block of code in a function is very advantageous since you can execute the code as many times as you want with a function call. 

## 2. When does the code in a function execute: when the function is defined or when the function is called?

When the function is called.

## 3. What statement creates a function?

The `def` statement

---
def < function_name > (< arguments >):
&nbsp;&nbsp;&nbsp;&nbsp;Statements`

---

## 4. What is the difference between a function and a function call?

A function refers to the block of code under the `def` statement.<br />
A function call makes the program execute the particular function.

## 5. How many global scopes are there in a Python program? How many local scopes?
One global scope.<br />
A local scope exists whenever a function or a loop is executed.

## 6. What happens to variables in a local scope when the function call returns?

The local scope and the variables in the function gets destroyed.

## 7. What is a return value? Can a return value be part of an expression?

The return value is the value a function call evaluates to.<br />
A return value can be a part of an expression.

## 8. If a function does not have a return statement, what is the return value of a call to that function?

`None`

## 9. How can you force a variable in a function to refer to the global variable?

`global < variable_name >`

## 10. What is the data type of None ?

`NoneType`

## 11. What does the import areallyourpetsnamederic statement do?

`import areallyourpetsnamederic`

The statement imports the module areallyourpetsnamederic to the program.
## 12. If you had a function named bacon() in a module named spam , how would you call it after importing spam ?

spam.bacon()

## 13. How can you prevent a program from crashing when it gets an error?

We can prevent a program from crashing by placing a `try:` and `except:` clause in the code, mentioning a message or instructions when a particular error comes.

## 14. What goes in the try clause? What goes in the except clause?
The code that can cause an error goes to `try:` clause.
The code that executes if an error happens goes to `except:` clause.
