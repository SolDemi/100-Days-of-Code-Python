from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
Off = False

while not Off:
    user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if user_choice == "report":
        coffee_machine.report()
        money_machine.report()
    elif user_choice == "off":
        Off = True
    else:
        beverage = menu.find_drink(user_choice)
        try:
            if coffee_machine.is_resource_sufficient(beverage):
                if money_machine.make_payment(beverage.cost):
                    coffee_machine.make_coffee(beverage)
        except AttributeError:
            pass
