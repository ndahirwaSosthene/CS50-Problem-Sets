import csv
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

var = sys.argv[1]

if not var.endswith('.csv'):
    sys.exit("Not a CSV file")

from tabulate import tabulate

table = []

try:
    with open(var) as file:
        reader = csv.DictReader(file)
        for row in reader:
            table.append(row)
        
    print(tabulate(table, headers="keys", tablefmt= "grid"))

except FileNotFoundError:
    print("File does not exist")