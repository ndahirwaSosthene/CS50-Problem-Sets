txt = input("Input: ").strip()

for c in txt:
    if c == "a" or c == "i" or c == "u" or c == "e" or c == "o" or c == "A" or c == "I" or c == "U" or c == "E" or c == "O":
        txt = txt.replace(c, "")
    else:
        exit

print(txt)
