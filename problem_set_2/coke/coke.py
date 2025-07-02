amount = 50
coin = 0
totalpaid = 0
while amount > 0:
    print(f"Amount Due: {amount}")
    coin = int(input("Insert coin: "))
    if coin == 10 or coin == 25 or coin == 5:
        totalpaid += coin
        amount -= coin
    else:
        coin = 0
print(f"Change Owed: {0}")

change = totalpaid - 50
if change > 0:
    print(f"Change Owed: {change}")

