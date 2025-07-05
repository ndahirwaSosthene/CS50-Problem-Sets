# Create menu dictionary
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
# Set total amount to 0
total = 0

# Loop forever
while True:
    try:
        # Get User input Title cased. That is to mean than any input will be turned into a title
        item = input("Item: ").title()

        # Check if item is already in the dictionary
        if item in menu:
            # Add the item price to the current price
            total = total + menu[item]
            # Print the current price
            print(f"Total: ${total:.2f}")
        
    except EOFError:
        # Print a new line and stop the loop
        print()
        break
    