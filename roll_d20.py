# this program rolls a d20 and prints the result
import random

roll = random.randrange(1, 21)

print('You rolled: ', roll)

repeat = input('Would you like to roll again? ')
repeat = repeat.lower()

while repeat == 'yes':
    if repeat == 'yes':
        roll = random.randrange(1, 21)
        print('You rolled: ', roll)
        repeat = input('Would you like to roll again? ')
        repeat = repeat.lower()

