# Number-Guessing Game

import random

num = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

while guess != num:
    if guess < num:
        print("Your guess is too low.")
    elif guess > num:
        print("Your guessis too high.")

    guess = int(input("Guess again: "))
                
print("You guessed it right.")

