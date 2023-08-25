from art import logo
from os import system
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def next_card(hand, score):
    next_card = random.choice(cards)
    new_score = score + next_card
    if next_card == cards[0] and new_score > 21:
        next_card = 1
        new_score = score + next_card
    hand.append(next_card)
    return hand, new_score

def ace(card1, card2, score):
    score = card1 + card2
    if card1 == cards[0] and score > 21:
        card1 = 1
        score = card1 + card2
    if card2 == cards[0] and score > 21:
        card2 = 1
        score = card1 + card2
    return card1, card2, score

def new_game():
    player_cards = []
    pc_cards = []
    player_score = 0
    pc_score = 0

    print(logo)
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    player_cards[0], player_cards[1], player_score = ace(player_cards[0], player_cards[1], player_score)

    pc_cards.append(random.choice(cards))

    print(f"    Your cards: {player_cards}, current score: {player_score}")

    final_hand = False
    while player_score < 21 and final_hand == False:
        print(f"    Computer's first card: {pc_cards[0]}")
        choice = input("Type 'y' to  get another card, type 'n' to pass: ").lower()
        if choice == 'n':
            final_hand = True
            print(f"    Your final hand: {player_cards}, final score: {player_score}")
        elif choice == 'y':
            player_cards, player_score = next_card(player_cards, player_score)
            print(f"    Your cards: {player_cards}, current score: {player_score}")

    pc_cards.append(random.choice(cards))
    pc_cards[0], pc_cards[1], pc_score = ace(pc_cards[0], pc_cards[1], pc_score)
    if pc_score < 17:
        pc_cards, pc_score = next_card(pc_cards, pc_score)
    print(f"    Computer's final hand: {pc_cards}, final score: {pc_score}")

    if player_score == pc_score:
        print("It's a draw!")
    elif pc_score > 21:
        print("Opponent went over. You win 😁")
    elif player_score > 21:
        print("You went over. You lose 😭")
    else:
        player_for_win = 21 - player_score
        pc_for_win = 21 - pc_score
        if player_for_win < pc_for_win:
            print("You win 😃")
        else:
            print("You lose 😤")

    game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if game == 'y':
        system("cls")
        new_game()

game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if game == 'y':
    system("cls")
    new_game()
