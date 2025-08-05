# Re-requesting a Vanity Plate

This program checks whether a Massachusetts vanity license plate is valid based on specific rules:

## Starts with at least two letters

## Contains 2 to 6 characters (letters or numbers)

## Numbers, if any, come only at the end and the first number isn’t zero

## No spaces, punctuation, or periods allowed

The function is_valid(s) takes a string and returns True if it meets all rules, else False.
The main() function prompts the user for a plate and prints Valid or Invalid. It runs only if the script is executed directly.

Run with:
**python plates.py**

# test_plates.py
This file contains multiple test functions beginning with test_ that thoroughly check your is_valid function for correctness.

Run tests with:
**pytest test_plates.py**
This structure supports modularity and easy testing for your vanity plates validator.