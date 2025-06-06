import random

secret_number = random.randint(1, 5)

guess = int(input("Guess a number from 1 to 5: "))

if guess < secret_number:
    print("Too low!")
elif guess > secret_number:
    print("Too high!")
elif guess == secret_number:
    print("You win!")
else:
    print("Invalid input")