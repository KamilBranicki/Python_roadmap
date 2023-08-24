from art import logo
from os import system

print(logo)
print("Welcome to the secret auction program.")

bid_dictionary = {}
next = True
while next:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    bid_dictionary[name] = bid

    next_choice = input("If there is next player type 'yes' or to close the auction type 'no': ").lower()

    if next_choice == "no":
        next = False
    system("cls")

max = 0
for key in bid_dictionary:
    if bid_dictionary[key] > max:
        max = bid_dictionary[key]
        winner = key

print(f"The winner is {winner} with bid ${max}")
