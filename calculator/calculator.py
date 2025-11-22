def add(n1, n2):
    """Adds two numbers."""
    return n1 + n2

def subtract(n1, n2):
    """Subtracts the second number from the first."""
    return n1 - n2

def multiply(n1, n2):
    """Multiplies two numbers."""
    return n1 * n2

def divide(n1, n2):
    """Divides the first number by the second. Handles Division by Zero error."""
    if n2 == 0:
        return "Error: Cannot divide by zero!"
    return n1 / n2

def calculator():
    """Main function to run the console calculator."""

    print("Welcome to the Simple Console Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("-" * 30)


    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }

    while True:

        choice = input("Enter choice (1/2/3/4/5): ")


        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break


        if choice in operations:
            try:

                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue


            function = operations[choice]
            result = function(num1, num2)


            print("-" * 30)
            print(f"Result: {num1} {['+', '-', '*', '/'][int(choice)-1]} {num2} = {result}")
            print("-" * 30)

        else:
            print("Invalid input. Please select a valid operation (1-5).")


if __name__ == "__main__":
    calculator()