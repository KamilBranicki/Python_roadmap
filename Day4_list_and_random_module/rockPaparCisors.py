import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
player = int(input("What do you choose: 0 for Rock, 1 for Paper, 2 for Scissors:"))
pc = random.randint(0,2)
game = [rock, paper, scissors]
if player < 0 or player > 3:
    print("Invalid number")
else:
    print(game[player])
    print("Computer chose:")
    print(game[pc])

    if player == pc:
        print("It is a draw")
    elif player < 0 or player > 3:
        print("Invalid number")
    elif player == 0 and pc == 1:
        print("Winner is PC")
    elif player == 0 and pc == 2:
        print("Winner is Player")
    elif player == 1 and pc == 0:
        print("Winner is Player")
    elif player == 1 and pc == 2:
        print("Winner is PC")
    elif player == 2 and pc == 0:
        print("Winner is PC")
    elif player == 2 and pc == 1:
        print("Winner is Player")
    else:
        print("Invalid number")