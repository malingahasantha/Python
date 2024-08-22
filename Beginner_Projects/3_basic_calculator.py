"""
Define a function needed : add, sub, mul, div
print option to the user
ask for values
Call the function
while loop to continue the program until the user wants to exit
"""

def add(a, b):
    answer = a+b
    return answer

def sub(a, b):
    answer = a-b
    return answer

def mul(a, b):
    answer = a*b
    return answer

def div(a, b):
    answer = a/b
    return answer

while True:
    print("A. Addition")
    print("B. Substraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Enter your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("Enter first value: "))
        b = int(input("Enter second value: "))
        addition = add(a,b)
        print(f'{a} + {b} = {addition} \n')
    elif choice == "b" or choice == "B":
        print("Substraction")
        a = int(input("Enter first value: "))
        b = int(input("Enter second value: "))
        substraction = sub(a,b)
        print(f'{a} - {b} = {substraction} \n')
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("Enter first value: "))
        b = int(input("Enter second value: "))
        multiplication = mul(a,b)
        print(f'{a} * {b} = {multiplication} \n')
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("Enter first value: "))
        b = int(input("Enter second value: "))
        division = div(a,b)
        print(f'{a} / {b} = {division} \n')
    elif choice == "e" or choice == "E":
        print("Exit")
        quit()
