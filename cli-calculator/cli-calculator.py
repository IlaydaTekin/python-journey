"""
CLI Calculator
A simple command-line calculator built with Python.
"""

def greet(name):
    print("Hello", name)

def show_menu():
    print("Choose one:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

def calculator(a,b,operator):
    if operator=="+":
        return a+b
    elif operator=="-":
        return a-b
    elif operator=="*":
        return a*b
    elif operator=="/":
        if b==0:
            return "Division error."
        else:
            return a/b
    else:
        return "Invalid operator"
    

name=input("Enter your name:")
greet(name)

while True:
    show_menu()

    a=float(input("First number: "))
    b=float(input("Second number: "))
    choise=input("Your choise: ")

    if choise=="1":
        operator="+"
    elif choise=="2":
        operator="-"
    elif choise=="3":
        operator="*"
    elif choise=="4":
        operator="/"
    else:
        operator="You chose invalid operator."
        continue

    result=calculator(a,b,operator)
    print("Result:",result)

    continue_process=input("Shall we continue?: (yes/no)").lower()
    if continue_process=="no":
        print("The program is finished.")
        break