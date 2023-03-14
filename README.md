# Coding Standards Exercise

This is a collection of python scripts to improve based on coding standards following PEP8 and Clean Code.

## Instructions

Identify coding standard issues within the code snippets.

Coding standards are important as they help programmers to code in a consistent style making the code more readable and thus easier to maintain.

Use the following resources to get some knowledge and understanding before attempting the exercises at the end of this tutorial sheet which will help you to practice your knowledge of coding:

Resources to help you with the Coding standards exercise:

1. A summary of python code style conventions
   https://development.robinwinslow.uk/2014/01/05/summary-of-python-code-style-conventions/
2. PEP 8 Style Guide for Python Code and Linters
   http://pep8.org/ &, https://www.python.org/dev/peps/pep-0008/
   https://www.youtube.com/watch?v=fFY5103p5-c

## Python Coding Standards

The following exercises are based on [PEP8](https://peps.python.org/pep-0008/) and Clean Code by Robert C. Martin.

## Exercises

| Exercise                                 |
| ---------------------------------------- |
| [Exercise 1](./exercises/exercise1.py)   |
| [Exercise 2](./exercises/exercise2.py)   |
| [Exercise 3](./exercises/exercise3.py)   |
| [Exercise 4](./exercises/exercise4.py)   |
| [Exercise 5](./exercises/exercise5.py)   |
| [Exercise 6](./exercises/exercise6.py)   |
| [Exercise 7](./exercises/exercise7.py)   |
| [Exercise 8](./exercises/exercise8.py)   |
| [Exercise 9](./exercises/exercise9.py)   |
| [Exercise 10](./exercises/exercise10.py) |
| [Exercise 11](./exercises/exercise11.py) |

## Answers

| Answers                                                                                                                                                                                                                                                            | Link                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------- |
| Indentation should be 4 spaces                                                                                                                                                                                                                                     | [1](./exercises/exercise1.answer.py)   |
| Every new import should be on a new line                                                                                                                                                                                                                           | [2](./exercises/exercise2.answer.py)   |
| Consistency - use either single quotes or double quotes for consistency unless for exceptions (e.g when a string contains a single quote)                                                                                                                          | [3](./exercises/exercise3.answer.py)   |
| Use multiline docstring for functions/classes that require more explanations                                                                                                                                                                                       | [4](./exercises/exercise4.answer.py)   |
| Class names should begin with uppercase. For example, "class base()" should be "class Base()"                                                                                                                                                                      | [5](./exercises/exercise5.answer.py)   |
| Constants should be all uppercase (e.g "i_am_a_constant" should be "I_AM_A_CONSTANT")                                                                                                                                                                              | [6](./exercises/exercise6.answer.py)   |
| The function name is not descriptive for what the function does. it should be called "get_database_uri". "uri" as the function name could mean anything                                                                                                            | [7](./exercises/exercise7.answer.py)   |
| the variable names 'fn', 'sn' and 'db' does not make sense. Use descriptive and understandable variable names. (e.g 'firstname', 'last_name', 'date_of_birth')                                                                                                     | [8](./exercises/exercise8.answer.py)   |
| The sum function does too many things... adds, finds percentage and prints. it should only do one job which is add numbers (Single-responsibility)                                                                                                                 | [9](./exercises/exercise9.answer.py)   |
| The two functions are similar. A single function with arguments can be written to calculate the percentage (DRY - Don’t Repeat Yourself)                                                                                                                           | [10](./exercises/exercise10.answer.py) |
| Too complicated to understand. Refactor the code such as spitting into multiple functions or use existing functions so that it is kept simple (KISS - Keep it simple, stupid). It replaces every character of the word argument within the text argument with `*`. | [11](./exercises/exercise11.answer.py) |
