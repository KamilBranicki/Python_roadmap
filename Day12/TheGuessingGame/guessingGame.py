from art import logo
from os import system
import random

def guess(attempts):
    while attempts != 0:
        guess = int(input("Make a guess: "))
        if guess < random_num:
            attempts -= 1
            print("Too low.\nGuess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")
        elif guess > random_num:
            attempts -= 1
            print("Too high.\nGuess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")
        else:
            print("You have won!")
            break
    print("You have lost!")

numbers = []
for i in range (1,101):
    numbers.append(i)

random_num = random.choice(numbers)\

print(logo)
print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
print(f"You have {attempts} attempts remaining to guess the number.")

guess(attempts)
