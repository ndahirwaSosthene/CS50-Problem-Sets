import re
# import sys                  


def main():
    print(f"\n{parse(input("HTML: "))}")


def parse(url):
    match = re.search(r'<iframe.*src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_]+)"', url)
    if match is None:
        return None
    else:
        embeded = match.group(1)
        new_embed = "https://youtu.be/" + embeded
        return new_embed

if __name__ == "__main__":
    main()