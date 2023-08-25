import random
from os import system
from hangman_art import logo, stages
from hangman_words import word_list
print(logo)
word = random.choice(word_list)
print(f"DEBUG CHEAT: {word}")

blank_word = []
for i in range(0,(len(word))):
    blank_word.append("_")

end_of_game = False
lives = 6
score = 0
guessed_word = ""
while not end_of_game:
    print(f"{' '.join(blank_word)}")
    letter = input("Pleae guess the letter: ").lower()
    system('cls')
    print(logo)
    letter_count = 0
    if letter in blank_word:
        print(f"You have already guessed letter {letter}")
    else:
        if letter not in word:
            lives -= 1
            print(f"In the word, there is no letter {letter}. You have lost a life")
        else:
            for i in range(0,(len(word))):
                if word[i] == letter:
                    blank_word[i] = letter
            score +=1
            
    print(stages[lives])
        
    if lives == 0:
        end_of_game = True
        print(f"The word is: {word}")
        print("You lost!")

    if score == len(word):
        end_of_game = True
        for i in range(0,len(blank_word)):
            guessed_word += blank_word[i]
        print(f"The word is: {guessed_word}")
        print("You won!")

