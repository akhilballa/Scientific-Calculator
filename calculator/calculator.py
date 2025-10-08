import math

def square_root(x):
    """Return the square root of x."""
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(x)

def factorial(x):
    """Return factorial of x."""
    if x < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    return math.factorial(x)

def natural_log(x):
    """Return natural logarithm (base e) of x."""
    if x <= 0:
        raise ValueError("Logarithm undefined for zero or negative numbers.")
    return math.log(x)

def power(x, b):
    """Return x raised to the power b."""
    return math.pow(x, b)


def main():
    print("\n🧮 Scientific Calculator")
    print("----------------------------")

    while True:
        print("\nSelect an operation:")
        print("1. Square Root (√x)")
        print("2. Factorial (!x)")
        print("3. Natural Logarithm (ln x)")
        print("4. Power Function (x^b)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        try:
            if choice == '1':
                x = float(input("Enter number: "))
                print("Result:", square_root(x))

            elif choice == '2':
                x = int(input("Enter integer: "))
                print("Result:", factorial(x))

            elif choice == '3':
                x = float(input("Enter number: "))
                print("Result:", natural_log(x))

            elif choice == '4':
                x = float(input("Enter base: "))
                b = float(input("Enter exponent: "))
                print("Result:", power(x, b))

            elif choice == '5':
                print("Exiting calculator... 👋")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError as e:
            print("Error:", e)
        except Exception as e:
            print("Unexpected error:", e)

if __name__ == "__main__":
    main()
