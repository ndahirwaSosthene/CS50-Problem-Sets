import sys
import argparse

count = 0
lines = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

var = sys.argv[1]

if not var.endswith('.py'):
    sys.exit("Not a Python file")

try:
    with open(var, 'r') as file:
        for line in file:
            if line.lstrip().startswith('#'):
                continue
            elif line.strip() == "":
                continue
            else:
                count += 1

    print(f'there are {count} lines')

except FileNotFoundError:
    sys.exit("File does not exist")