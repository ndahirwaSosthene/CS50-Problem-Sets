# Frank, Ian and Glen’s Letters

figlet.py is a program that generates large ASCII art text using FIGlet fonts, via the Python pyfiglet module.

The script can be run in two ways:

With no arguments: prompts for text and outputs it in a random FIGlet font.

With two arguments: use -f or --font followed by a font name to output text in a specific font.

If invalid arguments or font names are provided, the program exits with an error message.

This program uses the pyfiglet module.
Install it first with:

 # pip install pyfiglet

Run with
         **python figlet.py** (for random font) or
         **python figlet.py -f fontname** (for a specific font), then enter your text to see it as ASCII art.
Created for a CS50 exercise on command-line arguments, third-party modules, and ASCII art.

