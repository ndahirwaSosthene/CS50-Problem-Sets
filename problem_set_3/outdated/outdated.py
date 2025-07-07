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
    "December"
]

while True:
    date = input("Date: ")
    try:
        month, day, year = date.split("/")
        month = int(month.removesuffix(" "))
        day = int(day)
        year = int(year.removesuffix(" "))
        if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            print(year, f"{month:02}", f"{day:02}", sep="-")
            break
    except:
        try:
            if "," not in date:
                raise SyntaxError
            else:
                word_month, day, year = date.split(" ")
                day = day.replace(",", "")
                day = int(day)
                year = int(year)
                if word_month in months and (int(day) >= 1 and int(day) <= 31):
                    month = (months.index(word_month)+1)
                    print(year, f"{month:02}", f"{day:02}", sep="-")
                    break
        except:
            pass
