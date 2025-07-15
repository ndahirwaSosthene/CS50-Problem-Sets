def main():
    answer = input("Greeting: ").strip().lower()
    result = value(answer)
    print(result, end="")


def value(greeting):
    if greeting.__contains__("hello"):
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"
    
if __name__ == "__main__":
    main()
