# Testing my twttr

This program reimplements Setting up my twttr from CS50’s Problem Set 2 by restructuring the code into functions.

shorten(word)
A function that takes a string input and returns the same string with all vowels (A, E, I, O, U, both uppercase and lowercase) removed.

main()
Prompts the user for a string, calls shorten on it, and prints the result.

Run the program with:

bash
python twttr.py
test_twttr.py — Unit Tests for shorten
This file contains one or more test functions beginning with test_ that verify different aspects of the shorten function using pytest.

These tests cover inputs such as:

## Strings with uppercase and lowercase vowels

## Strings with no vowels

## Empty strings

## Strings containing only vowels

## Strings containing numbers and special characters (unchanged except vowels removed)

Run all tests by executing:

**pytest test_twttr.py**
Green lights mean tests passed; red means tests failed.

# How to use
Implement twttr.py with the described structure and vowel removal logic.

Implement test_twttr.py with thorough tests for your shorten function.

Run tests regularly to ensure correctness.

This refactor encourages modular design, easier testing, and better code reuse — essential skills in software development!

make sure to make it brief and simple yet informative
Here’s a brief, simple, and informative README for your twttr.py refactor and tests:

# twttr.py
This program shortens text by removing all vowels (A, E, I, O, U) from a user’s input.

shorten(word): takes a string and returns it without vowels.

main(): gets input from the user, calls shorten, and prints the result.

Run with:
**python twttr.py**
