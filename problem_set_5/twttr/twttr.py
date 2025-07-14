def main():
    txt = input("Input: ").strip()
    short = shorten(txt)
    print(short)

def shorten(word):
    for c in word:
        if c in ['a','e','i','u','o','A','E','I','U','O']:
            word = word.replace(c, "")
        else:
            exit
    return word

if __name__ == "__main__":
    main()

 