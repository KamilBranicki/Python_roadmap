from art import logo
from os import system

def plus(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": plus,
    "-": minus,
    "*": multiply,
    "/": divide
}
def new_calculation():
    system("cls")
    print(logo)
    appOn = True
    next = False
    num1 = 0
    while appOn:
        if next == False: 
            num1 = float(input("What's the first number?: "))
        for key in operations:
            print(key)
        sign = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        function = operations[sign]
        result = function(num1, num2)

        print(f"{num1} {sign} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation: ")

        if choice == "y":
            num1 = result
            next = True
        else:
            appOn = False
            new_calculation()
new_calculation()
    