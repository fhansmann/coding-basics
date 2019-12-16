## Purpose

This folder includes basic user created functions with the goal to built a tic-tac-toe game

## Table of Contents

  - [Basic Functions](basic-functions.py)
  - [Tic Tac Toe](game.py)

## Notes

Functions
- A function in Python is defined with the "def" keyword
- "return" is how a function gives back a value
- Functions include parameters (e.g. name, age, etc.)
- Argmuments can be formatted (format()) into a function (e.g. jack, 34, etc.)
	- Positioning argument vs. Keyword argument
- For functions, default parameters come last
- Foo function put a local variable inside the function, which will be defined by the user when the function is called
- "*" (star operator) for arguments ("args"): used to pack and unpack; pack arguments into a tuple inside fuctions (useful when you don't how many arguments you will have) or unpack them as arguments when you put them in to function
- ** for keyword arguments ("kwargs"; keyword and value): unpack keyword arguments into dictionary inside a function or pack them into a dictionary {} for your function to loop through them


Lambda (Anonymous) Functions
(Anayonmous because of "()")

Python code to illustrate cube of a number  
Showing difference between def() and lambda()

def cube(y): 
    return y*y*y; 
print cube(2)


g = lambda x: x*x*x 
print(g(2))

Note: Lambda definition does not include a “return” statement, it always contains an expression which is returned

Lambda functions can be used along with built-in functions like filter(), map() and reduce().
- Map: Apply the same set of steps to each item, storing the result.
- Filter: Apply validation criteria, storing items that evaluate True.
- Reduce: Return a value that is passed from element to element.

Each technique will require a function to be passed, which will be executed for each item. Often, the function is written as an anonymous function "=>" (called a fat arrow function in JavaScript).
However, in Python you often see lambda expressions being used.

One key difference between arrow functions and lambda expressions is that arrow functions are able to expand into full-blown functions with multiple statements while lambda expressions are limited to a single expression that is returned. Thus, when using map(), filter(), or reduce() if you need to perform multiple operations on each item, define your function first then include it.

def inefficientSquare(number):
   result = number * number
   return resultmap(inefficientSquare, my_list)


Note that map() and filter() are natively available. However, reduce() must be imported from the functools library

## Built With

- The code challenge solutions use [Python](https://www.python.org/)


