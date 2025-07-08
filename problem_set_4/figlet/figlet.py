import sys
import argparse
from pyfiglet import Figlet
import random

figlet = Figlet()
parser = argparse.ArgumentParser(description="Create your custom figlets:  Frank, Ian, and Glen’s letters")
parser.add_argument("-f","--font", help="Set font for your figlet text")
parser.add_argument("-l","--list", help="view all fonts available", action="store_true")
args , unknown= parser.parse_known_args()

if args.list:
    for font in figlet.getFonts():
        print(font)
    sys.exit(0)

if args.font:
    figlet.setFont(font = args.font)
elif unknown:
    print("Invalid usage")
    sys.exit(1)

else:
    figlet.setFont(font=random.choice(figlet.getFonts()))

text = input("Input: ")
print(figlet.renderText(text))


