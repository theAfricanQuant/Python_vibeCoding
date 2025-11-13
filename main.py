import math


def main():
    try:
        num_str = input("Enter a non-negative integer: ")
        num = int(num_str)
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = math.factorial(num)
            print(f"The factorial of {num} is {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
