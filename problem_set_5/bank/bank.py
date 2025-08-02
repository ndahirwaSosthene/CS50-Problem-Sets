def main():
    answer = input("Greeting: ")
    result = value(answer)
    print(f"${result}")


def value(greeting):
    # Normalize the input string inside the function being tested.
    cleaned_greeting = greeting.lower().strip()
    if cleaned_greeting.startswith("hello"):
        return 0
    elif cleaned_greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
