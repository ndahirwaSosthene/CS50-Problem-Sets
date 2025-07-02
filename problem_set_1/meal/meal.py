def main():
    time = input("What time is it: ")

    if 7.0 <= convert(time) <= 8.0:
        print("breakfast time")
    elif 12.0 <= convert(time) <= 13.0:
        print("lunch time")
    elif 18.0 <= convert(time) <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes)
    if minutes < 60:
        min = minutes/60
        tm = float(hours) + min
        return tm
    else:
        print("minutes out of range")

if __name__ == "__main__":
    main()
