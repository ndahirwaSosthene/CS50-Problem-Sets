# List of months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    date = input("Date:").strip().title()
    print(f"Got User input of: {date}")
    try:
        month, day, year = date.split("/")
        print(f"Date split into: month:{month}, day:{day}, year:{year}")
        if (int(month) >=1 and int(month) <=12) or (int(day) >=1 and int(day) <= 31):
            print(f"month{month} and day{day} are in the correct scope. Moving to printing new formatted date")
            break
    except:
        print("Seems like your date is in the word Month format, lets try that")
        try:
            old_month, old_day, old_year = date.split(" ")
            print(f"Date split by space into: month: {old_month}, day: {old_day}, year: {old_year}")
            day = int(old_day.removesuffix(","))
            print(f"day changed from {old_day} to {day}")
            if old_month in months:
                print(f"Checking if the month is in the months list{months}")
                month = months.index(old_month) + 1
                print(f"Since month: {old_month} is in months, we turned it into number: {month}")
            else:
                print("Oops, Month is not in months, we are going to have to reprompt you")
                break         
        except:
            print("Invalid input still, we will have to reprompt")
            pass

print("Made to a valid date, here is your new formatted date")
print(f"{year}-{int(month):02}-{int(day):02}")