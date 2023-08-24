from os import system
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     new_position = 0
#     for j in range (0,len(plain_text)):
#         new_position = alphabet.index(plain_text[j])+shift_amount
#         if new_position > len(alphabet):
#             new_position = new_position - len(alphabet)
#         cipher_text += (alphabet[new_position])
#     return cipher_text

# def decrypt(cipher_text,shift_amount):
#     plain_text = ""
#     new_position = 0
#     for j in range (0,len(cipher_text)):
#         new_position = alphabet.index(cipher_text[j])-shift_amount
#         if new_position < 0:
#             new_position = len(alphabet) - new_position
#         plain_text += (alphabet[new_position])
#     return plain_text

def cesar(text, shift, direction):
    cesar_text = ""
    new_position = 0

    if direction == "decode":
        shift *= -1

    for char in text:
        if char in alphabet:
            new_position = alphabet.index(char)+shift
            while new_position < 0:
                new_position = new_position + 52
            while new_position > 51:
                new_position = new_position - 52
            cesar_text += (alphabet[new_position])     
        else:
            cesar_text += char    
    return cesar_text
     
appOff = False
while appOff != True:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print(cesar(text = text, shift = shift, direction = direction))

    # if direction == "encode":
    #     text = input("Type your message:\n").lower()
    #     shift = int(input("Type the shift number:\n"))
    #     cipher_text = encrypt(plain_text = text, shift_amount = shift)
    #     print(cipher_text)
    # elif direction == "decode":
    #     text = input("Type your message:\n").lower()
    #     shift = int(input("Type the shift number:\n"))
    #     plain_text = decrypt(cipher_text = text, shift_amount = shift)
    #     print(plain_text)
    # else:
    #     print("Wrong commend")

    again = input("Do you want to continue? Type 'yes' to continue, type 'no' to finish:\n").lower()
    if again == "no":
        appOff = True
    elif again == "yes":
        appOff = False
    else:
        print("Wrong commend")
    system('cls')
