#Python picks a random number between 1 and 10
#The player types a guess
#Python says "Too low", "Too high", or "Correct!"
#The game keeps asking until the player gets it right

import random

difficulty = input("Choose a difficulty level (easy, medium, hard): ")

if difficulty == "easy":
    number = random.randint(1,10)
    attempts = 5
    print(f"You have {attempts} attempts to guess the number between 1 and 10.")
elif difficulty == "medium":
    number = random.randint(1,50)
    attempts = 15
    print(f"You have {attempts} attempts to guess the number between 1 and 50.")
elif difficulty == "hard":
    number = random.randint(1,100)
    attempts = 20
    print(f"You have {attempts} attempts to guess the number between 1 and 100.")

guess = int(input(" Guess the number: "))

while number != guess and attempts > 0:
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    attempts -= 1
    print(f"You have {attempts} attempts left.")
    if attempts > 0:
        guess = int(input(" Guess the number: "))
if guess == number:
    print("Correct! You got it right!")
else:    
    print(f"Game over dumb ass! The number was {number}. Try again when you're good at guessing.")