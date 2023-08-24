from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# 1.TODO: input dla kawy po każdej zakończonej akcji
# 2.TODO: 'off' w input to wyłączenie maszyny
# 3.TODO: 'report' w input to pokazanie obecnych środków maszyny
# 4.TODO: “Sorry there is not enough water." jeśli środki są niewystarczające do zrobienia zamówienia
# 5.TODO: jeśli środki są ok to prompt dla usera do włożenia kasy i zliczenie jej (quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01)
# 6.TODO: Sprawdzenie czy dobra ilość kasy została włożona do wymaganej ceny. Jeśli za mało to "Sorry that's not enough money. Money refunded."" Jęsli równa kasa to dodanie kasy do profitu. Jeśli za dużo zapłacił to wydaje reszte
# 7.TODO: Po zapłaceniu, wykoannie zamówienia, czyli obniżenie środków i: “Here is your latte. Enjoy!”.

menu = Menu()
actionCoffeMaker = CoffeeMaker()
money = MoneyMachine()

while True:
    order = input(f"What would you like? {menu.get_items()}:").lower()
    if order == "off":
        break
    elif order == "report":
        actionCoffeMaker.report()
        money.report()
    else:
        item = menu.find_drink(order) 
        if item:
            if actionCoffeMaker.is_resource_sufficient(item) and money.make_payment(item.cost):
                actionCoffeMaker.make_coffee(item)
