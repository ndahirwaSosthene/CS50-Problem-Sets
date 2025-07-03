# Meal Time

meal.py is a simple program that tells you which meal it’s time for based on the current time.

The program prompts the user to enter a time in 24-hour format (e.g., 7:30 or 12:00).
It outputs breakfast time if the time is between 7:00 and 8:00, lunch time if between 12:00 and 13:00, and dinner time if between 18:00 and 19:00 (all inclusive).
If the time doesn’t fall within any meal period, nothing is printed.

The script includes a convert function that converts the time string to a float representing hours.

Run with python meal.py and enter a time to find out which meal you should have!
Created for a CS50 exercise on string manipulation and conditional logic.