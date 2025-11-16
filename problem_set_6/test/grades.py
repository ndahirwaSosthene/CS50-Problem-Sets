import sys
import csv

if len(sys.argv) < 1:
    print('Too few command-line arguments')
if len(sys.argv) > 2:
    print('Too many command-line arguments')

file = sys.argv[1]

scores = []

with open(file) as input:
    reader = csv.DictReader(file)
    for row in reader:
        scores.append(row)

print(scores)