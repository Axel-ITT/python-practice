import random


def getInput():
    try:
        return int(input("Guess a number from 1 to 5: "))
    except ValueError as e:
        print("Sorry, that's not a number. You Failed.")
        print("Full Error: {}".format(e))

def check(guess):
    secret_number = random.randint(1, 5)
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("You win!")

while True:
    guess = getInput()
    if guess is not None:
        break
check(guess)