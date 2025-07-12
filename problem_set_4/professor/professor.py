import random


def main():
    level = get_level()#gets level of the numbers
    score = 0 #used to count the score to be displayed

    for _ in range(10): #looping ten times as in problem
        num1 = generate_integer(level) 
        num2 = generate_integer(level)
        result = num1 + num2
        tries = 0
        while tries < 3: # loop while the user only tries three times
            try:
                answer = int(input(f"{num1} + {num2} = "))
                if answer == result:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1
        else:
            print(f"{num1} + {num2} = {result}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()