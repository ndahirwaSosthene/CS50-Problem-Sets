try:
    while True:
        user_input = input("Enter text (Ctrl+D/Z to end): ")
        print(f"You entered: {user_input}")
except EOFError:
    print("EOF reached. No more input.")
