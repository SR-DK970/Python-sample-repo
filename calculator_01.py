import sys



from calculator_func import *

# Get the user's choice

while True:
    print("\nOperations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Enter the operation number: ")
    try:
        if choice == '5':
            print("Exiting the calculator...")
            break
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if choice == '1':
            addition = add(num1, num2)
            print("Result: ", addition)
        elif choice == '2':
            sub = subtract(num1, num2)
            print("Result: ", sub)
        elif choice == '3':
            mul = multiply(num1, num2)
            print("Result: ", mul)
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                div = divide(num1, num2)
                print("Result: ", div)
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Given input is not appropriate, please enter number")


# A test file for the calculator program using pytest









