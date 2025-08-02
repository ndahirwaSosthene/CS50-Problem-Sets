def shorten(word):
    """
    Takes a string as input and returns a new string
    with all vowels (a, e, i, o, u) removed, case-insensitively.
    """
    shortened_word = ""
    for letter in word:
        # Check if the lowercase version of the letter is a vowel
        if letter.lower() not in "aeiou":
            shortened_word += letter
    return shortened_word


def main():
    """
    Prompts the user for input, calls shorten, and prints the result.
    """
    user_input = input("Input: ")
    print("Output:", shorten(user_input))


if __name__ == "__main__":
    main()