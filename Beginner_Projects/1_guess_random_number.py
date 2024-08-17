import random

def guess_random(num):
    random_number = random.randint(1,num)
    guess_random = 0

    while(guess_random != random_number):
        guess_random = int(input(f'Guess a number between 1 and {num}: '))
        if guess_random < random_number:
            print('Sorry, guess again, too low!')
        elif guess_random > random_number:
            print('Sorry, guess again, too high!')
        
    print('Yey, congrats, you have guessed the number')

guess_random(12)

"""
random - Python has a built-in module that you can use to make random numbers.

The randint() method in random module returns an integer number selected element 
from the specified range.
"""
