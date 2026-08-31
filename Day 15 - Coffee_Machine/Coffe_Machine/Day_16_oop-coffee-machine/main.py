from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
while is_on:
    print("What can I serve you today between those drinks?")
    drink = input(f"{menu.get_items()}\n")

    if drink == "report":
        coffee_maker.report()
    elif drink == "money_report":
        money_machine.report()
    elif drink == "off":
        is_on = False
    elif menu.find_drink(drink):
        print(f"You chose {menu.find_drink(drink).name}")
        item_drink = menu.find_drink(drink)
        if coffee_maker.is_resource_sufficient(item_drink):
            print(f"Your {drink} is ready to be made, please pay ${(item_drink.cost):.2f}\n")
            if money_machine.make_payment(item_drink.cost):
                coffee_maker.make_coffee(item_drink)
                print(("Thank you for your payment and have a good day."))
            else:
                print("Sorry but not enough money was inserted.")
        else:
            print(f"Sorry, this machine doesn't have enough ingredients for your {drink}.")