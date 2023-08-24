import art
import random
from game_data import data
from os import system

score = 0

def draw():
    global data
    random_index = random.randint(0,len(data)-1)
    account = data[random_index]['name']
    followers = data[random_index]['follower_count']
    desc = data[random_index]['description']
    country = data[random_index]['country']
    data.pop(random_index)
    return account, followers, desc, country

a_account, a_followers, a_desc, a_country = draw()
b_account, b_followers, b_desc, b_country = draw()
a = [a_account, a_followers, a_desc, a_country]
b = [b_account, b_followers, b_desc, b_country]

while True:
    system("cls")
    print(art.logo)
    if score > 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {a[0]}, a {a[2]}, from {a[3]}. //{a[1]}")
    print(art.vs)
    print(f"Against B: {b[0]}, a {b[2]}, from {b[3]}. // {b[1]}")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if choice == 'a':
        if a[1] > b[1]:
            score += 1
            if score == 49:
                print("You won!")
                break
            b = draw()
        else:
            system("cls")
            print(f"Sorry, that's wrong. Final score: {score}")
            break
    elif choice == 'b':
        if b[1] > a[1]:
            score += 1
            if score == 49:
                print("You won!")
                break            
            a = b
            # for i in range(0,len(a)-1):
            #     a[i]=b[i]
            b = draw()
        else:
            system("cls")
            print(f"Sorry, that's wrong. Final score: {score}")
            break