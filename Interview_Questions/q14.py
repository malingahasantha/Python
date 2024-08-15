"""
Q14. Calculate the Fibonacci sequence up to user provided input.

Example: n=7, fib sequence = 0,1,1,2,3,5,8,13

Use:
1. User Input
2. Function
3. f.string

"""

fib_list = []

def fib(n):
    a = 0
    b = 1

    fib_list = [0,1]
    for i in range(2, n+1):
        c = a+b
        a = b
        b = c
        fib_list.append(c)
    return fib_list


user_input = input('Please enter a number: ')
number = int(user_input)
print(f'Fibonacci list of the entered number is: {fib(number)}')


# --------------------------- 2nd method -----------------------------

fib_list1 = []

def fib1(n): 
    fib_list1 = [0,1]
    while len(fib_list1) <= n:
        c = fib_list1[-1] + fib_list1[-2]
        fib_list1.append(c)
    return fib_list1

number1 = int(user_input)
print(f'Fibonacci list of the entered number is: {fib1(number1)}')