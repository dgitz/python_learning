import random
import sys

print('I am thinking of a number between 1 and 20.')
value = random.randint(1,20)
guessCount = 0
while True:
    print('Take a guess')
    guess = int(input())
    guessCount = guessCount + 1
    if guess == value:
        print('Good Job! You guessed my number in ' + str(guessCount) + ' guesses!')
        break
    elif guess < value:
        print('Your guess is too low.')
    elif guess > value:
        print('Your guess is too high.')

