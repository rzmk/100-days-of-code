from art import logo

#Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Calculator dict
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    num2 = float(input("What's the second number?: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation: ")
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    check = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")

    while check == "y":
        operation_symbol = input("Pick another operation: ")
        old_num = answer
        num3 = float(input("What's the next number?: "))
        answer = operations[operation_symbol](answer, num3)
        print(f"{old_num} {operation_symbol} {num3} = {answer}")
        check = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
    calculator()
calculator()