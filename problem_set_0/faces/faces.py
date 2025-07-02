def main():
    text = input("Enter any text: ")
    print(convert(text))

def convert(txt):
    if ":(" in txt or ":)" in txt:
        return txt.replace(":)","🙂").replace(":(","🙁")
    else:
        return txt

main()
