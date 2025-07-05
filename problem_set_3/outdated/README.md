# Outdated

outdated.py is a program that converts U.S.-style dates to the international ISO 8601 format.

The script prompts the user to enter a date in either numeric (e.g., 9/8/1636) or written (e.g., September 8, 1636) month-day-year format.
It outputs the same date in YYYY-MM-DD format, padding months and days with leading zeroes as needed.
If the input is not a valid date in either format, the program will prompt the user again until a valid date is entered.

Run with **python outdated.py** and enter a date to see it converted to ISO 8601 format.
Created for a CS50 exercise on string parsing, formatting, and input validation.