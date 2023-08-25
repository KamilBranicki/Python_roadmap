#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pass_letters = []
for n in range(0,nr_letters):
    random_letter = random.randint(1,len(letters))
    pass_letters.append(letters[random_letter-1])

pass_symbols = []
for m in range(0,nr_symbols):
    random_symbol = random.randint(1,len(symbols))
    pass_symbols.append(symbols[random_symbol-1])

pass_numbers = []
for x in range(0,nr_numbers):
    random_number = random.randint(1,len(numbers))
    pass_numbers.append(numbers[random_number-1])

passwordList = pass_letters+pass_symbols+pass_numbers
password = ''
for y in range(0,len(passwordList)):
    password += passwordList[y]
print("Easy level\nRandom password is:", password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

passwordListHard = []
passwordlen = nr_letters+nr_symbols+nr_numbers

while len(passwordListHard) !=  passwordlen:
    choice = random.choice(passwordList)
    passwordListHard.append(choice)
    passwordList.remove(choice)

password = ''
for z in range(0,len(passwordListHard)):
    password += passwordListHard[z]
print("\nHard level\nRandom password is:", password)