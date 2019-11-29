import random
import time

print("--------GUESS THE NUMBER--------\n"
      "Guess the number between 1 and 20\n"
      "You have 5 try")

number = random.randint(1, 20)
tryings = 5
while True:
    users_guess = int(input("\nEnter number:"))

    if users_guess == number:
        print("Congrats! Correct answer:",number)
        break

    elif users_guess > number:
        tryings -= 1
        if tryings == 0:
            print("No tryings left, game over!\n"
                  "Correct answer was:", number)
            break
        print("Guess Lower")
        print("Tryings left:",tryings)

    elif users_guess < number:
        tryings -= 1
        if tryings == 0:
            print("No tryings left, game over!\n"
                  "Correct answer was:", number)
            break
        print("Guess Higher")
        print("Tryings left:",tryings)


