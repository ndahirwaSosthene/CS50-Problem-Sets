import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(time):
    match = re.search(r'(\d{1,2}):?(\d{2})?\s(AM|PM)\sto\s(\d{1,2}):?(\d{2})?\s(AM|PM)', time)
    if match is None:
        raise ValueError


    start_hour = int(match.group(1))
    end_hour = int(match.group(4))

    start_period = match.group(3)
    end_period = match.group(6)

    start_minutes = match.group(2)
    end_minutes = match.group(5)
    
    if start_minutes == None:
        start_minutes = 0
    else:
        start_minutes = int(start_minutes)
    if end_minutes == None:
        end_minutes = 0
    else:
        end_minutes = int(end_minutes)

    if start_minutes > 59 or start_minutes < 0:
        raise ValueError
    
    if end_minutes > 59 or end_minutes < 0:
        raise ValueError
    
    if start_hour > 12 or start_hour < 1:
        raise ValueError
    
    if end_hour > 12 or end_hour < 1:
        raise ValueError

    if start_period == "AM":
        if start_hour == 12:
            start_time = f"{0:02}:{start_minutes:02}"
        else:
            start_time = f"{start_hour:02}:{start_minutes:02}"

    elif start_period == "PM":
        if start_hour == 12:
            start_time = f"{12:02}:{start_minutes:02}"
        else:
            start_time = f"{(start_hour+12):02}:{start_minutes:02}"

    if end_period == "AM":
        if end_hour == 12:
            end_time = f"{0:02}:{end_minutes:02}"
        else:
            end_time = f"{(end_hour):02}:{end_minutes:02}"

    elif end_period == "PM":
        if end_hour == 12:
            end_time = f"{12:02}:{end_minutes:02}"
        else:
            end_time = f"{(end_hour+12):02}:{end_minutes:02}"

    return f"{start_time} to {end_time}"

if __name__ == "__main__":
    main()