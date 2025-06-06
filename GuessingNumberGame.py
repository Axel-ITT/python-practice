import random

def print_NaN():
    print("          _____                    _____                    _____")
    print("         /\\    \\                  /\\    \\                  /\\    \\")
    print("        /::\\____\\                /::\\    \\                /::\\____\\")
    print("       /::::|   |               /::::\\    \\              /::::|   |")
    print("      /:::::|   |              /::::::\\    \\            /:::::|   |")
    print("     /::::::|   |             /:::/\\:::\\    \\          /::::::|   |")
    print("    /:::/|::|   |            /:::/__\\:::\\    \\        /:::/|::|   |")
    print("   /:::/ |::|   |           /::::\\   \\:::\\    \\      /:::/ |::|   |")
    print("  /:::/  |::|   | _____    /::::::\\   \\:::\\    \\    /:::/  |::|   | _____")
    print(" /:::/   |::|   |/\\    \\  /:::/\\:::\\   \\:::\\    \\  /:::/   |::|   |/\\    \\")
    print("/:: /    |::|   /::\\____\\/:::/  \\:::\\   \\:::\\____\\/:: /    |::|   /::\\____\\")
    print("\\::/    /|::|  /:::/    /\\::/    \\:::\\  /:::/    /\\::/    /|::|  /:::/    /")
    print(" \\/____/ |::| /:::/    /  \\/____/ \\:::\\/:::/    /  \\/____/ |::| /:::/    /")
    print("         |::|/:::/    /            \\::::::/    /           |::|/:::/    /")
    print("         |::::::/    /              \\::::/    /            |::::::/    /")
    print("         |:::::/    /               /:::/    /             |:::::/    /")
    print("         |::::/    /               /:::/    /              |::::/    /")
    print("         /:::/    /               /:::/    /               /:::/    /")
    print("        /:::/    /               /:::/    /               /:::/    /")
    print("        \\::/    /                \\::/    /                \\::/    /")
    print("         \\/____/                  \\/____/                  \\/____/")




def getInput():
    try:
        return int(input("Guess a number from 1 to 5: "))
    except ValueError as e:
        print_NaN()
        print(e)

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