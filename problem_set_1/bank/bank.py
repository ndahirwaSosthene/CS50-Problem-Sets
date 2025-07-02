answer = input("Greeting: ").strip().lower()

if answer.__contains__("hello"):
    print("$0", end="")
elif answer.startswith("h"):
    print("$20", end="")
else:
    print("$100", end="")
