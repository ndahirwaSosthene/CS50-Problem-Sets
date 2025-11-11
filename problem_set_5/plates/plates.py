def main():
    plate = input("Enter plate: ").strip().upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
    if not isinstance(s, str):
        return False

    s = s.strip()

    if not 2 <= len(s) <= 6:
        return False
    if not s.isalnum:
        return False
    
    if not(s[0].isalpha() and s[1].isalpha()):
        return False
    for i, ch in enumerate(s):
        if ch.isdigit():
            if ch == "0":
                return False
            if not s[i:].isdigit():
                return False
            return True
    return True
if __name__ == "__main__":
    main()
