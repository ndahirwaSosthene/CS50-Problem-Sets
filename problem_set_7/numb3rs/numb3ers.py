import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
    if match is None:
        return False
    for octet in match.groups():
        if octet.startswith('0') and len(octet) > 1:
            return False
        elif int(octet) > 255 or int(octet) < 0:
            return False

    return True



if __name__ == "__main__":
    main()