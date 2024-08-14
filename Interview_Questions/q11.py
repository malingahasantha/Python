"""
Q11. Check if a user input number is prime.

Prime number is only divisible by 1 and itself.
1 is not a prime number.

Use:
1. User Input
2. Function
3. f.string

Aditional task --> optimize the program
"""

def is_prime(number):
    if number < 2:
        return False
    
    for item in range(2, number):
        if number % item == 0:
            return False
        
    return True
        
user_input = input('Enter a Number: ')
number = int(user_input)

if is_prime(number):
    print(f'{number} is a Prime Number')
else:
    print(f'{number} is not a Prime Number')


# for item in range(2, number//2):

"""
In here we are dividing number from 2 to number, So if the number is like 254, then it will
divide the number 252 times. To optimeze this we can make it to half. if number 10 is not dividing 
from 2 to 5, it is not divide from 6 to 9 for sure. So we can make the division by half.

we can perform floor division (also sometimes known as integer division) using the // operator.
The result of regular division (using the / operator) is 15/4 = 3.75, but using // has floored 
3.75 down to 3.

print(15 / 4) --> 3.75
print(15 // 4) --> 3
"""

