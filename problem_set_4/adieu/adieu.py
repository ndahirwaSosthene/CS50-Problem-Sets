import inflect
names = []
while True:
    i = inflect.engine()
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        break

print(f"Adieu, adieu, to {i.join(names)}")