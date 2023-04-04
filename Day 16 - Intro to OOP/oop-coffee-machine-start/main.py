from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_maker = MoneyMachine()

while True:
    user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    if user_choice == "off":
        break

    if user_choice == "report":
        coffee_machine.report()
        money_maker.report()

    if user_choice in menu.get_items():
        selected_drink = menu.find_drink(user_choice)

        if selected_drink is not None:
            if coffee_machine.is_resource_sufficient(selected_drink):
                print(f"That will cost ${selected_drink.cost}.")
                if money_maker.make_payment(selected_drink.cost):
                    coffee_machine.make_coffee(selected_drink)
            else:
                print(f"Not enough resources")