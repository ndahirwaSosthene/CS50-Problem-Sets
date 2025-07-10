# Guessing Game

game.py is a number guessing game that challenges the user to guess a randomly generated integer.

The script works as follows:

1. Prompts the user to enter a level (the upper bound for the random number). Only positive integers are accepted.

2. Randomly selects an integer between 1 and the chosen level (inclusive).

3. Prompts the user to guess the number, accepting only positive integers.

After each guess, provides feedback:

- Outputs Too small! if the guess is less than the number.

- Outputs Too large! if the guess is greater than the number.

- Outputs Just right! and exits if the guess is correct.

This program uses Python’s built-in random module for number generation.

Run with **python game.py**, enter your level and guesses, and see if you can guess the number!
Created for a CS50 exercise on input validation, loops, and random number generation.

