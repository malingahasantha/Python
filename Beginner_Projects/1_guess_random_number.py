"""
Write a program to guess the random number generating from random module.

random - Python has a built-in module that you can use to make random numbers.

The randint() method in random module returns an integer number selected element 
from the specified range.
"""


import random

def guess_random(num):
    random_number = random.randint(1,num)
    guess = 0

    while(guess != random_number):
        guess = int(input(f'Guess a number between 1 and {num}: '))
        if guess < random_number:
            print('Sorry, guess again, too low!')
        elif guess > random_number:
            print('Sorry, guess again, too high!')
        
    print('Yey, congrats, you have guessed the number')

guess_random(12)


