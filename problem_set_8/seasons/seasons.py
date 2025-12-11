from datetime import date, datetime
import inflect
import sys

def main():
    date_of_birth = input("Date of Birth: ")
    try:
        print(calculate_minutes(date_of_birth))
    except ValueError:
        sys.exit(1)

def calculate_minutes(dob):
    try:
        format_string = "%Y-%m-%d"

        today = date.today()
        print(today)

        birth_date = datetime.strptime(dob, format_string).date()
        print(birth_date)

        days = today - birth_date
        print(days)

        minutes = days.days * 1440
        print(str(minutes))
        final = convert_to_words(minutes)
        return final
    except ValueError:
        raise ValueError

def convert_to_words(mins):
    p = inflect.engine()
    minutes_in_words = p.number_to_words(mins, andword='')
    return f"{minutes_in_words.capitalize()} minutes"


if __name__ == "__main__":
    main()