def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0] == "A-Z" and s[1] == "A-Z" and 2 <=len(s) <= 6:
        ...

main()
