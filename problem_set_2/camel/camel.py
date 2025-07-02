txt = input("Camel case: ")

for c in txt:
    if (c.isupper()):
        txt = txt.replace(c, f"_{c.lower()}")#this re assignment is to assess if anytime the program
                                            #finds a letter is capital it reassigns changes with the new letter changed to _(initial letter in lower case)
    else:
        exit

print(f"Snake case: {txt}")
