import random

while True:
    try:
        level = int(input("Level: "))
        if level < 0:
            break
        number = random.randint(1, level)
        break
    except ValueError:
        continue

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue
        elif guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        continue
