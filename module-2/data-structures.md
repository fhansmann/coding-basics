## Purpose

This file includes basic data structures such as lists and tupels and method to manipulate them

## Table of Contents

  - [Cinema](cinema.py)
  - [Travis](travis.py)

## Notes

Lists:
- Defined by enclosing a comma-separated sequence of objects in square brackets []
- Ordered collection of objects
- Individual elements can be accessed using an index in square brackets
 
 Tuples:
 Tuples are identical to lists in all respects, except for the following properties:
   - Tuples are defined by enclosing the elements in parentheses (()) instead of square brackets ([]).
   - Tuples are immutable
   - Even though tuples are defined using parentheses, you still index and slice tuples using square brackets, just as for strings and list

“Remove” keyword is used if you know specifically what to delete; else us delete (e.g. del “list name” [index]). The reasons being that the “remove” keyword only removes the first instance.

List methods: e.g. remove, append, insert, no re-assignment required ("="), otherwise the variable will be turned into non-type; example: A = a.remove(2) -> non-type (watch out!)

## Built With

- The code challenge solutions use [Python](https://www.python.org/)
