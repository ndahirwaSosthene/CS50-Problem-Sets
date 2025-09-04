import sys
import argparse

count = 0
lines = []

if len(sys.argv) > 1:
    print(sys.argv[0])
    print(sys.argv[1])
    name = sys.argv[1]
    if name.isalnum(): 
        if name.endswith(".py"):

            with open(name, "r") as file:
                lines = file.readlines()      
        else:
            print("Not a python file")
    else:
        print("Invalid/ non existing python file")
else:
    print("No files inputted")

for line in lines:
    if line.startswith("# ") or line.startswith(" "):
        count += 0
    else:
        count +=1

print(f"number of lines: {count}")