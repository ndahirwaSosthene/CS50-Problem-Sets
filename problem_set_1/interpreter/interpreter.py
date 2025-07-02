opera = input("Expression: ")

x,y,z = opera.split(" ")

match y:
    case "+":
        res = float(x) + float(z)
    case "-":
        res = float(x) - float(z)
    case "*":
        res = float(x) * float(z)
    case "/":
        res = float(x) / float(z)
    case "%":
        res = float(x) % float(z)
    case _:
        print("That is not a valid operator. ")

print(res)
