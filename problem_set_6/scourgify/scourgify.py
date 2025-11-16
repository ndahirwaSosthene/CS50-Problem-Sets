import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

var = sys.argv[1]

new_file = sys.argv[2]

if not var.endswith('.csv'):
    sys.exit("Not a CSV file")

people = []
formated_list = []

try:
    with open(var) as file:
        reader = csv.DictReader(file,)
        for row in reader:
            people.append(row)

    print(people)

except FileNotFoundError:
    print("File does not exist")

try:
    with open(new_file, 'w', newline="") as newfile:
        header = ['first', 'last', 'house']
        writer = csv.DictWriter(newfile, fieldnames=header)

        writer.writeheader()
        for row in people:
            last, first = row["name"].split(",")
            last = last.strip()
            first = last.strip()

            new_row = {"first": first, "last": last, "house": row["house"]}
            writer.writerow(new_row)

except FileNotFoundError:
    print("File does not exist")
    sys.exit