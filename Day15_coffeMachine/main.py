from machineData import MENU, resources
from os import system
profit = 0
flag_payed = 0

# 1.TODO: input dla kawy po każdej zakończonej akcji
# 2.TODO: 'off' w input to wyłączenie maszyny
# 3.TODO: 'report' w input to pokazanie obecnych środków maszyny
# 4.TODO: “Sorry there is not enough water." jeśli środki są niewystarczające do zrobienia zamówienia
# 5.TODO: jeśli środki są ok to prompt dla usera do włożenia kasy i zliczenie jej (quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01)
# 6.TODO: Sprawdzenie czy dobra ilość kasy została włożona do wymaganej ceny. Jeśli za mało to "Sorry that's not enough money. Money refunded."" Jęsli równa kasa to dodanie kasy do profitu. Jeśli za dużo zapłacił to wydaje reszte
# 7.TODO: Po zapłaceniu, wykoannie zamówienia, czyli obniżenie środków i: “Here is your latte. Enjoy!”.

def payment(cost,profit, order):
    quarters = 0.25 * int(input("quarters = "))
    dimes = 0.1 * int(input("dimes = "))
    nickles = 0.05 * int(input("nickles = "))
    pennies = 0.01 * int(input("pennies = "))
    payed = quarters + dimes +  nickles + pennies
    if payed < cost:
        print("Sorry that's not enough money. Money refunded.")
        return 0, 0
    elif payed == cost:
        profit = round(profit + cost,2)
        flag_payed = 1
        print(f"Here is the change ${change}")
        return profit, flag_payed
    elif payed > cost:
        change = round(payed - cost,2)
        profit = round(profit + cost,2)
        flag_payed = 1
        print(f"Here is the change ${change}")
        print(f"Here is your {order}. Enjoy! ☕")
        return profit, flag_payed
    



while True:
    order = input("What would you like? (espresso/latte/cappuccino):").lower()
    if order == "espresso":
        if resources["water"] >= MENU[order]["ingredients"]["water"]:
            if resources["coffee"] >= MENU[order]["ingredients"]["coffee"]:
                profit, flag_payed = payment(MENU[order]["cost"],profit)
            else:
                print("Sorry there is not enough coffee.")
        else:
             print("Sorry there is not enough water.")
    elif order == "latte" or order == "cappuccino":
        if resources["water"] >= MENU[order]["ingredients"]["water"]:
            if resources["milk"] >= MENU[order]["ingredients"]["milk"]:
                if resources["coffee"] >= MENU[order]["ingredients"]["coffee"]:
                    profit, flag_payed = payment(MENU[order]["cost"],profit, order)
                else:
                    print("Sorry there is not enough coffee.")
            else:
                print("Sorry there is not enough milk.")
        else:
             print("Sorry there is not enough water.")
    elif order == "report":
        for key in resources:
            if key == "profit":
                print(f"${key}: {resources[key]}")
            else:
                print(f"{key}: {resources[key]}")
    elif order == "off":
        system("cls")
        break
    
    if flag_payed == 1:
        resources["water"] = resources["water"] - MENU[order]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[order]["ingredients"]["coffee"]
        if order != "espresso":
            resources["milk"] = resources["milk"] - MENU[order]["ingredients"]["milk"]
        resources["profit"] = profit
        flag_payed = 0
