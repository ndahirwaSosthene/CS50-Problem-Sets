def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dol = d[1:]
    return float(dol)


def percent_to_float(p):
    per = p[:-1]
    return float(per)/100


main()
