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
    try:
        month, day, year = date.split("/")
        if (int(month) >=1 and int(month) <=12) or (int(day) >=1 and int(day) <= 31):
            break
    except:
        try:
            old_month, old_day, old_year = date.split(" ")
            day = int(old_day.removesuffix(","))
            year = old_year
            if old_month in months:
                month = months.index(old_month) + 1
                break
            else:
                break
        except:
            pass
        break

print(f"{year}-{int(month):02}-{int(day):02}")
