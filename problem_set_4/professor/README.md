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

# Little Professor

`professor.py` is a command-line math quiz game inspired by the classic "Little Professor" toy. The program quizzes the user with 10 random addition problems, adjusting the difficulty based on the selected level.

## How It Works

1. **Level Selection:**  
   The user is prompted to choose a level (1, 2, or 3):
   - Level 1: Single-digit numbers (0–9)
   - Level 2: Two-digit numbers (10–99)
   - Level 3: Three-digit numbers (100–999)

2. **Quiz Rounds:**  
   The program generates 10 random addition problems according to the chosen level. For each problem:
   - The user has up to 3 attempts to enter the correct answer.
   - If the answer is incorrect or not a number, the program prints `EEE`.
   - After 3 incorrect attempts, the correct answer is displayed and the game moves to the next problem.

3. **Scoring:**  
   The user's score increases by 1 for each correct answer (within 3 tries). At the end, the total score out of 10 is displayed.
