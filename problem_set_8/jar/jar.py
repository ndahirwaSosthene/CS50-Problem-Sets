import sys

class Jar:
    def __init__(self, capacity=12):
        if isinstance(capacity, int) and capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError
        self.cookies = 0

    def __str__(self):
        return "🍪"*self.cookies

    def deposit(self, n):
        if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
            raise ValueError
        else:
            self.remaining = self.capacity - self.size
            if self.remaining < n:
                raise ValueError
            else:
                self.cookies += n

    def withdraw(self, n):
        if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
            raise ValueError
        else:
            if n > self.size:
                raise ValueError
            else:
                self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

# NOTE: so there is a difference between self.capacity(public but for readonly) and self._capacity(private that can be written on)

    @property
    def size(self):
        return self.cookies

def main():
    try:
        new_jar = Jar(capacity=int(input("Enter Jar capacity: ")))
        print(f"Jar capacity: {new_jar.capacity}")
    except ValueError:
        print("Invalid capacity")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nExiting program...")
        sys.exit(1)

    try:
        new_jar.deposit(n=int(input("Enter Number of New Cookies: ")))
        print("Depositing ...")
        print(f"Cookies in the jar: {new_jar.size} \nin cookies: \n{new_jar.__str__()}")
    except ValueError:
        print("Invalid number of cookies")
        # sys.exit(1)
    except KeyboardInterrupt:
        print("\nExiting program...")
        sys.exit(1)

    try:    
        new_jar.withdraw(n=int(input("Enter Number of Cookies to Eat: ")))
        print("Withdrawing ...")
        print(f"Cookies in the jar: {new_jar.size} \nin cookies: \n{new_jar.__str__()}")
    except ValueError:
        print("Invalid Number of Cookies")
        # sys.exit(1)
    except KeyboardInterrupt:
        print("\nExiting program...")
        sys.exit(1)

if __name__ == "__main__":
    main()