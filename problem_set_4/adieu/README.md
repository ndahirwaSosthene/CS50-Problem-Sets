# Adieu, Adieu

adieu.py is a program that bids farewell to a list of names in the style of "The Sound of Music."

The script prompts the user to enter names one per line until control-d (EOF) is pressed.
It then prints a farewell message, formatting the names correctly with commas and "and" (using the Oxford comma as needed), e.g.,
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt.

This program uses the inflect module to handle proper English joining of names.
Install it first with:

 # pip install inflect

Run with **python adieu.py**, enter your names, and press control-d to see the farewell message.
Created for a CS50 exercise on list handling, string formatting, and third-party modules.